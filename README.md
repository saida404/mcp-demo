Use-case ovog mog servera je simulacija finansijskog agenta za upravljanje računima, jer je to problem koji je blizak našem stvarnom problemu.  
Ideja je da AI agent može koristiti dostupne tools za unos, praćenje, "plaćanje" i generisanje izvještaja.  
Ja sam koristila Python, te SQLite lokalnu bazu podataka.

Day 1:  
Uradila sam osnovne stvari i postavila osnovni kostur za zadatak.  
Koristim SQLite lokalnu bazu koja za sad sadrži par osnovnih tabela koje omogućavaju unos, praćenje i generisanje izvještaja.  
Napravila sam neke jednostavne tools kako bih testirala da li sve funkcioniše kako treba.  
Claude trenutno uspješno koristi dostupne tools, vrši upisivanja u bazu, ažuriranja i generisanje izvještaja.  

Sljedeći korak je poboljšanje postojećih tools-a tako da budu "realističniji", bolji error handling,  
dodavanje novih funkcionalnosti i ispunjavanje zadatih kriterija :D  

Day 2:  
Nastavila sam raditi na poboljšanju postojećih funkcionalnosti servera, dodala sam bolju validaciju i error handling,  
te sam probala tools učiniti malo realističnijim i sigurnijim za korištenje od strane agenta.  
Dalje želim dodati i neki resource, testirati rad servera i poboljšati ga.  
Claude je povezan sa serverom i radi za sada sve što treba.  

Dalje dodati neki resource i prompt, fine-tunati postojeće tools.


Struktura projekta:
- database/ - rad sa lokalnom bazom podataka, CRUD
- tools/ - logika koju koriste mcp tool funkcije
- main.py - FastMCP server i registracija alata
- tests/ - testovi za logiku alata

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


pokretanje MCP servera : python main.py
pokretanje testova: pytest ili detaljnjije pytest -v