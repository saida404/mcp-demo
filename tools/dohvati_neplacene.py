from database.crud import get_neplaceni
from tools.pomocne.pomocna import handle_tool_errors

@handle_tool_errors
def tools_dohvati_neplacene(id_korisnik: int):


    result = get_neplaceni(id_korisnik)

    return result