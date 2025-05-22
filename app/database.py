import sqlite3
import os
from contextlib import contextmanager

DATABASE_URL = "app/meditrack.db"

@contextmanager
def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with sqlite3.connect(DATABASE_URL) as conn:
        cursor = conn.cursor()
        print("Using database at:", os.path.abspath(DATABASE_URL))

        
        # Drop existing tables (for clean re-init)
        cursor.execute("DROP TABLE IF EXISTS appointments")
        cursor.execute("DROP TABLE IF EXISTS symptoms")
        cursor.execute("DROP TABLE IF EXISTS medications")
        
        # Recreate with correct schema
        cursor.execute("""
            CREATE TABLE appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                date TEXT NOT NULL, 
                description TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE symptoms (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                date TEXT NOT NULL, 
                symptom TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE medications (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL, 
                dosage TEXT NOT NULL
            )
        """)
        conn.commit()


init_db()
