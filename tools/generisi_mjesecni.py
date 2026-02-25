from database.crud import get_izvjestaj_podaci
from tools.pomocne.pomocna import handle_tool_errors, normalizuj_input_mjeseca

ID_KORISNIK = 1

@handle_tool_errors
def tools_izvjestaj(
                    mjesec: str,
                    godina: int):
    


    mjesec_norm = normalizuj_input_mjeseca(mjesec)

    result = get_izvjestaj_podaci(ID_KORISNIK,mjesec_norm,godina)
    return result
     