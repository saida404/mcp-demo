from database.crud import kreiraj_racun

def tools_dodaj_racun(id_korisnik: int,
                      tip_racuna: str, 
                      iznos: float, 
                      rok_uplate: str, 
                      mjesec: str):
    return kreiraj_racun(id_korisnik, tip_racuna, iznos,rok_uplate,mjesec)