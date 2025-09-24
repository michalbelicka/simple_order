import sqlite3

def create_db():
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            address TEXT,
            product TEXT,
            quantity INTEGER      
     )
    """)
    
    conn.commit()
    conn.close()

create_db()