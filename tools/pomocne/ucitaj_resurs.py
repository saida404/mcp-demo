from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RESOURCES_DIR = PROJECT_ROOT / "resources"
CONFIG_PATH = RESOURCES_DIR / "ogranicenja_za_placanja.json"
SAVJETI_PATH = RESOURCES_DIR / "finansijski_savjeti.json"


def ucitaj_ogranicenja():
    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data  
    except Exception as e:
        print(f"Greška pri učitavanju fajla: {e}")
        return {"ogranicenja": {}}
    
def ucitaj_savjete():
    try:
        with SAVJETI_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("savjeti", [])  
    except Exception as e:
        print(f"Greška pri učitavanju fajla: {e}")
        return {"savjeti": []}