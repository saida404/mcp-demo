from .crud import kreiraj_racun, get_racuni_od_korisnika, plati_racun, get_izvjestaj_podaci
from .konekcija import get_connection

def test_connection():
        conn = get_connection()
        conn.close()
  

if __name__ == "__main__":
   # test_connection()
    print("-------------")
   # kreiraj_racun(1, 2, 120.6, "2026-03-01", "maj")

    print("+++++++++")
    print(get_racuni_od_korisnika(1))
    print("++++++++++++++++++")

   # plati_racun(1,2,"maj")
    print(get_izvjestaj_podaci(1,"maj"))