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
from tools.tools_mail import tools_posalji_mail


@mcp.tool()
def dodaj_racun_tool(tip_racuna: str, iznos: float, rok_uplate: str, mjesec: str, godina: int):
    """ Tool dodaje novi racun za korisnika u bazu podataka.

    Koristi ovaj tool kada korisnik zatraži dodavanje novog računa, kada agent dobije informacije o računu koji nije u bazi.
      
      Parametri:
    - tip_racuna: (string) mora biti jedan od [struja, voda, plin, komunalije, telefon, internet]
    - iznos: (float) iznos računa
    - rok_uplate: (string), datum u formatu YYYY-MM-DD
    - mjesec: (sting) 
    -godina (integer)

    """    
    return tools_dodaj_racun(tip_racuna, iznos, rok_uplate, mjesec, godina)


@mcp.tool()
def plati_racun_tool(tip_racuna: str, mjesec: str, godina: int):
    """ Tool placa racun za korisnika, 

    Koristi ovaj tool kada korisnik želi platiti račun i kada korisnik potvrdi da želi platiti račun nakon 
    što agent prikaže informacije o računu i upozori na rok uplate.
    
    Parametri:
    tip racuna (string) moze biti neki od: struja, voda, plin, komunalije, telefon, internet
    mjesec (string) i godina (integer)
       """
    return tools_plati_racun(tip_racuna, mjesec, godina)

@mcp.tool()
def izvjestaj_tool(mjesec: str, godina: int):
    """  Generiše mjesečni izvještaj za korisnika.

    Koristi kada korisnik zatraži izvještaj za određeni mjesec i godinu, 
    ili kada agent želi ponuditi generisanje izvještaja nakon što korisnik plati račun.

    Parametri:
    mjesec (string) i godina (integer)
    
    """
    return tools_izvjestaj(mjesec,godina)


@mcp.tool()
def dohvati_neplacene_tool() :
    """ Dohvaća listu neplaćenih računa za korisnika.
    
    Koristi kada korinsik želi vidjeti koje račune ima neplaćene.

    Tools ne prima parametre jer uvijek vraća listu aktivnih neplaćenih računa
    
    """
    return tools_dohvati_neplacene()

@mcp.tool()
def posalji_mail_duplikat_tool(tip_racuna: str, mjesec: str, godina: int):
    """Tool šalje mail pružaocu usluga kada je detektovan duplikat računa.
    Koristi ovaj tool kada dodavanje računa vrati grešku duplikata i korisnik potvrdi slanje maila.
    
    Parametri:
    - tip_racuna: (string) tip računa za koji je detektovan duplikat
    - mjesec: (string) mjesec računa
    - godina: (integer) godina računa
    """
    return tools_posalji_mail(tip_racuna, mjesec, godina)

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
