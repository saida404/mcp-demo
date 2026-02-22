from database.exceptions import ValidationError, NotFoundError, DatabaseError

def handle_tool_errors(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            return {
                "success": True,
                "data": result
            }

        except ValidationError as e:
            return {"success": False, "error": str(e)}
        
        except ValueError as e:
            return {"success": False, "error": str(e)}

        except NotFoundError as e:
            return {"success": False, "error": str(e)}

        except DatabaseError:
            return {"success": False, "error": "Interna greska baze podataka"}

        except Exception:
            return {"success": False, "error": "Neocekivana greska"}

    return wrapper


ALLOWED_MJESECI = {
    "januar","februar","mart","april","maj","juni",
    "juli","avgust","septembar","oktobar","novembar","decembar"
}

def normalizuj_input_mjeseca(mjesec: str):
    if not mjesec:
        raise ValueError("Mjesec nije unesen")
    
    mjesec = mjesec.strip().lower()

    if mjesec not in ALLOWED_MJESECI:
        raise ValueError(
            "Nepoznat mjesec. Dozvoljeno: januar, februar, mart, april, maj, juni, juli, avgust, septembar, oktobar, novembar, decembar"
        )

    return mjesec


