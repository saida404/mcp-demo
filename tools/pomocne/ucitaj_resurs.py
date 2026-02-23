import json
import os

CONFIG_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "resources",
    "ogranicenja_za_placanja.json"
)

def ucitaj_ogranicenja():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return json.dumps(data)
    except Exception:
        return json.dumps({"ogranicenja": {}})