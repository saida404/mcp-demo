from database.crud import get_neplaceni
from tools.pomocne.pomocna import handle_tool_errors

ID_KORISNIK = 1

@handle_tool_errors
def tools_dohvati_neplacene():


  return  get_neplaceni(ID_KORISNIK)

  