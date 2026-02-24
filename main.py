from mcp.server.fastmcp import FastMCP
from pathlib import Path
import logging
from typing import Dict, Any, Union


mcp = FastMCP("moj-server")

from tools.dodaj_racun import tools_dodaj_racun
from tools.plati_racun import tools_plati_racun
from tools.generisi_mjesecni import tools_izvjestaj
from tools.dohvati_neplacene import tools_dohvati_neplacene
from tools.pomocne.ucitaj_resurs import ucitaj_ogranicenja



@mcp.tool()
def dodaj_racun_tool(id_korisnik: int, tip_racuna: str, iznos: float, rok_uplate: str, mjesec: str, godina: int):
    """ Tool dodaje novi racun za korisnika u bazu podataka.
      
      Parametri:
    -id_korisnik: (integer) ID korisnika
    - tip_racuna: (string) mora biti jedan od [struja, voda, plin, komunalije, telefon, internet]
    - iznos: (float) iznos računa
    - rok_uplate: (string), datum u formatu YYYY-MM-DD
    - mjesec: (sting) 
    -godina (integer)

    """    
    return tools_dodaj_racun(id_korisnik, tip_racuna, iznos, rok_uplate, mjesec, godina)


@mcp.tool()
def plati_racun_tool(id_korisnik: int, tip_racuna: str, mjesec: str, godina: int):
    """Tool placa racun za korisnika, 
    Parametri:
    id kornisnika(int) koji placa racun, 
    tip racuna (string) moze biti neki od: struja, voda, plin, komunalije, telefon, internet
    mjesec (string) i godina (integer)
       """
    return tools_plati_racun(id_korisnik, tip_racuna, mjesec, godina)

@mcp.tool()
def izvjestaj_tool(id_korisnik: int, mjesec: str, godina: int):
    """  Generise mjesecni izvještaj za korisnika.
    Parametri:
    id korisnika (integer)
    mjesec (string) i godina (integer)
    
    """
    return tools_izvjestaj(id_korisnik,mjesec,godina)


@mcp.tool()
def dohvati_neplacene_tool(id_korisnik: int) :
    """ Dohvata listu neplacenih racuna za korisnika.
    Parametri:
    id korisnika (integer)
    
    """
    return tools_dohvati_neplacene(id_korisnik)

@mcp.resource("placanje://ogranicenja")
def ogranicenja_resource():
    """ Resource koji agent koristi za čitanje limita plaćanja. """
    return ucitaj_ogranicenja()

@mcp.prompt()
def billing_assistant_prompt():
    """System prompt za asistenta."""
    return """
    Ti si ljubazni i profesionalni asistent za upravljanje komunalnim računima.

    Tvoje glavne odgovornosti su:
    - Pregled neplaćenih računa korisnika
    - Plaćanje računa na zahtjev korisnika
    - Dodavanje novih računa
    - Generisanje mjesečnih izvještaja

    Pravila ponašanja:
    - Uvijek se obraćaj korisniku ljubazno i profesionalno
    - Prije svake akcije provjeri da li imaš ID korisnika
    - Nakon plaćanja računa uvijek potvrdi uspješnost akcije
    - Ako korisnik želi platiti sve račune odjednom, uradi to redom jedan po jedan
    - Upozoravaj korisnika na račune kojima se bliži rok uplate
    -Ako iznos računa prelazi 100 KM, obavezno zatraži potvrdu od korisnika prije plaćanja. 
    Jasno prikaži iznos i pitaj: "Račun iznosi više od 100KM. Da li ste sigurni da želite izvršiti plaćanje?" Nastavi s plaćanjem samo ako korisnik eksplicitno potvrdi.   

    Dostupni tipovi računa: struja, voda, plin, komunalije, telefon, internet.

    Primjer pozdrava:
    "Dobrodošli! Ja sam vaš asistent za upravljanje računima. 
    Kako vam mogu pomoći danas?"
    """


if __name__ == "__main__":
    mcp.run() 
