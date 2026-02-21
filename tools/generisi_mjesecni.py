from database.crud import get_izvjestaj_podaci

def tools_izvjestaj(id_korisnik: int,
                    mjesec: str):
    try:
        result = get_izvjestaj_podaci(id_korisnik,mjesec)

        return {
            "success" : True,
            "data": result
        }
    except Exception as e:
        return{
            "success": False,
            "error": str(e)
        }