
from database.konekcija import get_connection
from database.exceptions import  (ValidationError, NotFoundError, AlreadyPaidError, DatabaseError)

ALLOWED_TIPOVI =  {"struja", "voda", "plin", "internet", "telefon", "komunalije" }

def validate_tip(tip_racuna):
    if not tip_racuna:
        return False

    return tip_racuna.lower() in ALLOWED_TIPOVI

def kreiraj_racun(id_korisnik, tip_racuna, iznos, rok_uplate, mjesec, godina):
    
    tip_racuna = tip_racuna.lower()

    if not validate_tip(tip_racuna):
        raise ValidationError("Tip racuna nije dozvoljen")

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""select id_racuni from Racuni where id_korisnik = ? and tip_racuna = ? and mjesec = ? and godina = ? """, (id_korisnik, tip_racuna, mjesec, godina))

        postoji = cursor.fetchone()

        if postoji:
            raise ValidationError(f"Za {mjesec}/{godina} je već pristigao račun za {tip_racuna}")
        
        cursor.execute("""
            insert into Racuni(id_korisnik, tip_racuna, iznos, rok_uplate, mjesec, godina) values (?,?,?,?,?,?)                   
    """, (id_korisnik, tip_racuna, iznos, rok_uplate, mjesec, godina))
        
        connection.commit()
        connection.close()
    except ValidationError:
        raise

    except Exception as e:
        raise DatabaseError(f"Greska baze: {str(e)}")
    



def get_racuni_od_korisnika(id_korisnik):
    try: 
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            select * from Racuni where id_korisnik = ?
    """, (id_korisnik,))
        
        rows = cursor.fetchall()
        connection.close()
        
        return [dict(row) for row in rows]
    
    except Exception as e:
        raise DatabaseError(f"Greska pri dohvacanju racuna: {str(e)}")


def get_neplaceni(id_korisnik):
    try: 
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""select * from racuni where id_korisnik = ? and placeno = 0 """, (id_korisnik,))

        rows = cursor.fetchall()
        connection.close()

       
        return [dict(row) for row in rows]

    except Exception as e:
        raise DatabaseError(f"Greska pri dohvacanju neplacenih racuna: {str(e)}")


    
def plati_racun(id_korisnik, tip_racuna, mjesec, godina):
    tip_racuna = tip_racuna.lower()

    try: 
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""select id_racuni from Racuni where id_korisnik = ? and tip_racuna = ? and mjesec = ? and godina = ? and placeno = 0 """, (id_korisnik, tip_racuna, mjesec, godina))

        racun = cursor.fetchone()

        if not racun:
            connection.close()
            raise NotFoundError("Racun ne postoji ili je vec placen")
        id_racuni = racun["id_racuni"]

        cursor.execute("""update Racuni set placeno = 1 where id_racuni = ? """, (id_racuni,))

        connection.commit()
        connection.close()
        
    except NotFoundError:
        raise

    except Exception as e:
        raise DatabaseError(f"Greska pri placanju racuna: {str(e)}")





def get_izvjestaj_podaci(id_korisnik, mjesec, godina):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            select 
                count(*) as pristiglo_racuna,
                sum(iznos) as ukupno_za_platiti,
                sum(case when placeno = 1 then iznos else 0 end) as ukupno_placeno,
                sum(case when placeno = 0 then iznos else 0 end) as ukupno_neplaceno
            from racuni
            where id_korisnik = ?
            and mjesec = ? and godina = ?
                       
        """, (id_korisnik, mjesec, godina))

        stats = cursor.fetchone()
        connection.close()

        return {
            "mjesec": mjesec,
            "godina": godina,
            "pristiglo_racuna": stats["pristiglo_racuna"] or 0,
            "ukupno_za_platiti": round(stats["ukupno_za_platiti"] or 0, 2),
            "ukupno_placeno": round(stats["ukupno_placeno"] or 0, 2),
            "ukupno_neplaceno": round(stats["ukupno_neplaceno"] or 0, 2)
        }

    except Exception as e:
        raise DatabaseError(f"Greska baze: {str(e)}")
    

def sacuvaj_izvjestaj_history(id_korisnik, mjesec, report_data):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        insert into izvjestaji(
            id_korisnik,
            mjesec,
            pristiglo_racuna,
            ukupno_za_platiti,
            ukupno_placeno,
            ukupno_neplaceno
        ) values (?,?,?,?,?,?)
    """, (
        id_korisnik,
        mjesec,
        report_data["pristiglo_racuna"],
        report_data["ukupno_za_platiti"],
        report_data["ukupno_placeno"],
        report_data["ukupno_neplaceno"]
    ))

    connection.commit()
    connection.close()