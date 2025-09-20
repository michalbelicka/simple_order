import sqlite3

def insert_orders(name, email, address, product, quantity):
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            address TEXT,
            product TEXT,
            quantity INTEGER      
     )
    """)
    
    conn.commit()
    conn.close()