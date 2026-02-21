from database.crud import plati_racun

def tools_plati_racun(id_korisnik: int,
                     tip_racuna: str, 
                     mjesec: str):
    return plati_racun(id_korisnik, tip_racuna, mjesec)