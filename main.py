from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("moj-server")

from tools.dodaj_racun import tools_dodaj_racun
from tools.plati_racun import tools_plati_racun
from tools.generisi_mjesecni import tools_izvjestaj

@mcp.tool()
def dodaj_racun_tool(id_korisnik: int, tip_racuna: str, iznos: float, rok_uplate: str, mjesec: str):
    """Dodaje novi racun za korisnika"""
    return tools_dodaj_racun(id_korisnik, tip_racuna, iznos, rok_uplate, mjesec)


@mcp.tool()
def plati_racun_tool(id_korisnik: int, tip_racuna: str, mjesec: str):
    """Placa racun za korisnikaw"""
    return tools_plati_racun(id_korisnik, tip_racuna, mjesec)

@mcp.tool()
def izvjestaj_tool(id_korisnik: int, mjesec: str):
    return tools_izvjestaj(id_korisnik,mjesec)


if __name__ == "__main__":
    mcp.run() 
