Use-case ovog mog servera je simulacija finansijskog agenta za upravljanje računima, jer je to problem koji je blizak našem stvarnom problemu. Ideja je da AI agent može koristiti dostupne tools za unos, praćenje, "plaćanje" i generisanje izvještaja. Ja sam koristila Python, te SQLite lokalnu bazu podataka.

Day 1: Uradila sam osnovne stvari i postavila osnovni kostur za zadatak. Koristim SQLite lokalnu bazu koja za sad sadrži par osnovnih tabela koje omogućavaju unos, praćenje i generisanje izvještaja. Napravila sam neke jednostavne tools kako bih testirala da li sve funkcioniše kako treba. Claude trenutno uspješno koristi dostupne tools, vrši upisivanja u bazu, ažuriranja i generisanje izvještaja.

(Sljedeći korak je poboljšanje postojećih tools-a tako da budu "realističniji", bolji error handling, 
   dodavanje novih funkcionalnosti i ispunjavanje zadatih kriterija :D)

Day 2: 
    Nastavila sam raditi na poboljsanju postojecih funkcionalnosti servera, dodala sam bolju validaciju i error handling, te sam probala tools ucinit malo realisticnim i sigurnijim za koristenje od strane agenta. Dalje zelim dodati i neki resource, testirati rad servera i poboljsati ga. Claude je povezan sa serverom i radi za sada sve sto treba.
(Dalje dodati neki resource i prompt, fine-tunati postojece tools,)
