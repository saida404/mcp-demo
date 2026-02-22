from mcp.server.fastmcp import FastMCP
from pathlib import Path
import logging


mcp = FastMCP("moj-server")

from tools.dodaj_racun import tools_dodaj_racun
from tools.plati_racun import tools_plati_racun
from tools.generisi_mjesecni import tools_izvjestaj
from tools.dohvati_neplacene import tools_dohvati_neplacene

@mcp.tool()
def dodaj_racun_tool(id_korisnik: int, tip_racuna: str, iznos: float, rok_uplate: str, mjesec: str, godina: int):
    """ Dodaje novi racun.
      Parametri:
    - id_korisnik: integer ID korisnika
    - tip_racuna: mora biti jedan od [struja, voda, plin, komunalije, telefon, internet]
    - iznos: iznos računa
    - rok_uplate: datum u formatu YYYY-MM-DD
    - mjesec: sting 
    -godina integer

    """    
    return tools_dodaj_racun(id_korisnik, tip_racuna, iznos, rok_uplate, mjesec, godina)


@mcp.tool()
def plati_racun_tool(id_korisnik: int, tip_racuna: str, mjesec: str, godina: int):
    """Placa racun za korisnika, tip racuna mora biti jedan od struja voda plin komunalije telefon internet, godina je integer, mjesec je string """
    return tools_plati_racun(id_korisnik, tip_racuna, mjesec, godina)

@mcp.tool()
def izvjestaj_tool(id_korisnik: int, mjesec: str, godina: int):
    """  Generise mjesecni izvještaj za korisnika.
    Parametri:
    id korisnika integer, mjesec string i godina integer
    
    """
    return tools_izvjestaj(id_korisnik,mjesec,godina)


@mcp.tool()
def dohvati_neplacene_tool(id_korisnik: int):
    """ Dohvata neplacene racune za korisnika.
    Parametri:
    id korisnika integer
    
    """
    return tools_dohvati_neplacene(id_korisnik)


if __name__ == "__main__":
    mcp.run() 
