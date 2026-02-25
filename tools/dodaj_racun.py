from database.crud import kreiraj_racun
from tools.pomocne.pomocna import handle_tool_errors, normalizuj_input_mjeseca

ID_KORISNIK = 1

@handle_tool_errors
def tools_dodaj_racun(
                      tip_racuna: str, 
                      iznos: int, 
                      rok_uplate: str, 
                      mjesec: str,
                      godina: int):
    
    mjesec_norm = normalizuj_input_mjeseca(mjesec)
    kreiraj_racun(ID_KORISNIK, tip_racuna, iznos,rok_uplate,mjesec_norm,godina)

    return {"status": "success", "message": "Racun kreiran"}