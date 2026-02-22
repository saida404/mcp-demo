from database.crud import get_izvjestaj_podaci
from tools.pomocne.pomocna import handle_tool_errors, normalizuj_input_mjeseca

@handle_tool_errors
def tools_izvjestaj(id_korisnik: int,
                    mjesec: str,
                    godina: int):
    


    mjesec_norm = normalizuj_input_mjeseca(mjesec)

    result = get_izvjestaj_podaci(id_korisnik,mjesec_norm,godina)
    return result
     