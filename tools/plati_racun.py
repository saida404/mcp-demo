from database.crud import plati_racun
from tools.pomocne.pomocna import handle_tool_errors, normalizuj_input_mjeseca


@handle_tool_errors
def tools_plati_racun(id_korisnik: int,
                     tip_racuna: str, 
                     mjesec: str,
                     godina: int):

    mjesec_norm = normalizuj_input_mjeseca(mjesec)

    plati_racun(id_korisnik, tip_racuna, mjesec_norm, godina)   

    return {"status": "success", "message": "Racun placen"}