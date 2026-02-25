from database.crud import plati_racun
from tools.pomocne.pomocna import handle_tool_errors, normalizuj_input_mjeseca

ID_KORISNIK = 1

@handle_tool_errors
def tools_plati_racun(
                     tip_racuna: str, 
                     mjesec: str,
                     godina: int):

    mjesec_norm = normalizuj_input_mjeseca(mjesec)

    plati_racun(ID_KORISNIK, tip_racuna, mjesec_norm, godina)   

    return {"status": "success", "message": "Racun placen"}