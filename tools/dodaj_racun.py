from database.crud import kreiraj_racun
from tools.pomocne.pomocna import handle_tool_errors, normalizuj_input_mjeseca

@handle_tool_errors
def tools_dodaj_racun(id_korisnik: int,
                      tip_racuna: str, 
                      iznos: int, 
                      rok_uplate: str, 
                      mjesec: str,
                      godina: int):
    
    mjesec_norm = normalizuj_input_mjeseca(mjesec)

  

    return kreiraj_racun(id_korisnik, tip_racuna, iznos,rok_uplate,mjesec_norm,godina)