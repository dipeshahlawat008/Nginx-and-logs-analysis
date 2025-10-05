# Minimal storage using sqlite for history (placeholder)
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'sentinelops.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS metrics (ts INTEGER, cpu REAL, mem REAL)''')
    conn.commit()
    conn.close()
