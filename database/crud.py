from database.konekcija import get_connection

ALLOWED_TIPOVI =  {"struja", "voda", "plin", "internet", "telefon"}

def validate_tip(tip_racuna):
    if not tip_racuna:
        return False

    return tip_racuna.lower() in ALLOWED_TIPOVI

def kreiraj_racun(id_korisnik, tip_racuna, iznos, rok_uplate, mjesec):
    
    tip_racuna = tip_racuna.lower()

    if not validate_tip(tip_racuna):
        return {
            "success" : False,
            "error" : "Tip racuna nije dozvoljen"
        }

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            insert into Racuni(id_korisnik, tip_racuna, iznos, rok_uplate, mjesec) values (?,?,?,?,?)                   
    """, (id_korisnik, tip_racuna, iznos, rok_uplate, mjesec))
        
        connection.commit()
        connection.close()

        return {"success": True,
            "message": "Racun uspjesno dodan"}

    except Exception as e:
        return {
            "success" : False,
            "error" : str(e)
        }
    



def get_racuni_od_korisnika(id_korisnik):
    try: 
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            select * from Racuni where id_korisnik = ?
    """, (id_korisnik,))
        
        rows = cursor.fetchall()
        connection.close()
        return { "success": True,
                "data": [dict(row) for row in rows]
        }
    except Exception as e:
        return {
            "success" : True,
            "error": str(e)
        }
    



def get_neplaceni(id_korisnik):
    try: 
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""select * from racuni where id_korisnik = ? and placeno = 0 """, (id_korisnik,))

        rows = cursor.fetchall()
        connection.close()

       
        return {
            "success": True,
            "data": [dict(row) for row in rows]
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e) }

    
def plati_racun(id_korisnik, tip_racuna, mjesec):
    tip_racuna = tip_racuna.lower()

    try: 
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""select id_racuni from Racuni where id_korisnik = ? and tip_racuna = ? and mjesec = ? and placeno = 0 """, (id_korisnik, tip_racuna, mjesec,))

        racun = cursor.fetchone()

        if not racun:
            connection.close()
            return {
                "success": False,
                "error": "Racun ne postoji ili je vec placen"
            }
        id_racuni = racun["id_racuni"]

        cursor.execute("""update Racuni set placeno = 1 where id_racuni = ? """, (id_racuni,))

        connection.commit()
        connection.close()
        return {
            "success": True,
            "message": "Racun je placen"
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }





def get_izvjestaj_podaci(id_korisnik, mjesec):

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
            and mjesec = ?
        """, (id_korisnik, mjesec))

        stats = cursor.fetchone()
        connection.close()

        return {
            "mjesec": mjesec,
            "pristiglo_racuna": stats["pristiglo_racuna"] or 0,
            "ukupno_za_platiti": round(stats["ukupno_za_platiti"] or 0, 2),
            "ukupno_placeno": round(stats["ukupno_placeno"] or 0, 2),
            "ukupno_neplaceno": round(stats["ukupno_neplaceno"] or 0, 2)
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
    

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