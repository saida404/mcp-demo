Ovo je moja ultra pojednostavljena verzija finansijskog agenta za upravljanje računima.
Izabrala sam ovaj usecase jer je blizak našem problemu kojim ćemo se baviti.

Tech stack: Python, FastMCP, SQLite


Struktura projekta:
- database/ - rad sa lokalnom SQL bazom podataka, CRUD operacije
- tools/ - logika koju koriste MCP tool funkcije
- main.py - FastMCP server i registracija alata
- tests/ - testovi za logiku alata
- screenshots/ - slike interakcije Claud Desktop sa ovim serverom


Tools:

- dodaj_racun_tool: dodaje račun u bazu podataka za korisnika ako on već nije dodan, ako račun za dati period i tip računa već postoje u bazi obavještava agenta te agent nudi slanje maila izdavaču računa.

        parametri: 
                   tip_racuna (string) -> vrsta računa (struja,voda,plin,komunalije,telefon,internet)
                   iznos (float) -> iznos računa
                   rok_uplate (string) -> rok plaćanja u formatu YYYY-MM-DD
                   mjesec (string) -> mjesec na koji se račun odnosi
                   godina (integer) -> godina na koju se odnosi

- plati_racun_tool: plaća (u ovom pojednostavljenom slučaju ažurira) račun korisnika

        parametri: 
                   tip_racuna (string)
                   mjesec(string) i godina (int)

- izvjestaj_tool: generiše kompletan mjesečni izvještaj za korisnika, plaćene i neplaćene račune i ukupne troškove

        parametri: 
                   mjesec (string)
                   godina (int)

- dohvati_neplacene_tool: dohvaća listu svih neplaćenih računa za korisnika

        parametri: bez parametara

 - posalji_mail_duplikat_tool: ukoliko se prilikom unosa računa u bazu desi da je za taj period već pristigao taj tip računa, agent obavještava korisnika i pita ga da li želi da pošalje mail izdavaču računa pitajući da li je greška.
 
    Parametri: 
        tip_racuna: str, 
        mjesec: str, 
        godina: int

Pokretanje:
1) kloniranje projekta:
    git clone  https://github.com/saida404/mcp-demo
    cd mcp-demo

2) kreiranje i aktivacija virtualnog okruzenja
    python3 -m venv venv
    (Mac/Linux) - > source venv/bin/activate 
    (Windows) - >  venv\Scripts\activate

3) instalacija potrebnih alata
    pip install -r requirements.txt

4) pokretanje MCP servera 
     python main.py

5) pokretanje testova: 
    pytest ili detaljnjije pytest -v

Projekt koristi lokalnu SQLite bazu za razvoj i testiranje. 
Baza nije uključena u repozitorij i potrebno ju je inicijalizirati prije pokretanja projekta.

--------------------------------------

Za daily progress updates pogledati notes_daily_progress.txt