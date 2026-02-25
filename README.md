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

- izvjesta_tool: generiše kompletan mjesečni izvještaj za korisnika, plaćene i neplaćene račune i ukupne troškove

        parametri: 
                   mjesec (string)
                   godina (int)

- dohvati_neplacene_tool: dohvaća listu svih neplaćenih računa za korisnika

        parametri: bez parametara

 - posalji_mail_duplikat_tool: ukoliko se prilikom unosa računa u bazu desi da je za taj period već pristigao taj tip računa, agent obavještava korisnika i pita ga da li želi da pošalje mail izdavaću računa pitajući da li je greška.
 
    Parametri: 
        tip_racuna: str, 
        mjesec: str, 
        godina: int

Pokretanje:
1) kloniranje projekta:
    git clone 
    cd server-proba

2) kreiranje i aktivacija virtualnog okruzenja
    python3 -m venv venv
    (Mac/Linux) - > source env/bin/activate 
    (Windows) - >  env\Scripts\activate

3) instalacija potrebnih alata
    pip install -r requirements.txt

4) pokretanje MCP servera 
     python main.py

5) pokretanje testova: 
    pytest ili detaljnjije pytest -v



--------------------------------------

My notes:

Day 1:  
Uradila sam osnovne stvari i postavila osnovni kostur za zadatak.  
Koristim SQLite lokalnu bazu koja za sad sadrži par osnovnih tabela koje omogućavaju unos, praćenje i generisanje izvještaja.  
Napravila sam neke jednostavne tools kako bih testirala da li sve funkcioniše kako treba.  
Claude trenutno uspješno koristi dostupne tools, vrši upisivanja u bazu, ažuriranja i generisanje izvještaja.  

Sljedeći korak je poboljšanje postojećih tools-a tako da budu "realističniji", bolji error handling,  
dodavanje novih funkcionalnosti i ispunjavanje zadatih kriterija 

Day 2:  
Nastavila sam raditi na poboljšanju postojećih funkcionalnosti servera, dodala sam bolju validaciju i error handling,  
te sam probala tools učiniti malo realističnijim i sigurnijim za korištenje od strane agenta.  
Dalje želim dodati i neki resource, testirati rad servera i poboljšati ga.  
Claude je povezan sa serverom i radi za sada sve što treba.  

Dalje dodati neki resource i prompt, fine-tunati postojeće tools.

Day 3 i 4:
Dodala sam resource i promt. Testirala do sada urađeno. Pokušati učiniti korišćenje toolsa više user-friendly, sredila sam readme, dodala screenshotove config fajla i interakcije Clauda sa serverom.

Day 5:
Uredila sam kod tako da agent više ne mora pitati za id_korisnika, već je id hardkodiran da je uvijek 1. Ažurirala sam testove da budu u skladu sa ovim promjenama. 

Dodala sam provjeru prilikom dodavanja računa u bazu. Ako račun za dati period (mjesec i godinu) tog tipa već postoji, agent nudi korisniku da pošalje mail izdavaču računa i pita o grešci i slično.
Ja sam ovdje koristila neki bezveze mail koji sam imala, radi testiranja. 
Agent jee uspio da detektuje dupli unos i ponudi slanje maila, te ga je nakon potvrde poslao (screenshot 10 i 11) 

(imala sam problema sa Claude Desktopom, izgleda da je bio neki globalni problem, pa sam 3 sata pokušala pronaći grešku misleći da je do mog servera)