import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "racuni.db")

def get_connection():
    try:
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        print("Konekcija je uspjesna!")
        return connection
    except Exception as e:
        print("konekcija nije uspjela ", e)
        raise