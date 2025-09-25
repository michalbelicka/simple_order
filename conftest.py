import sqlite3

def clear_db():
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("DELETE FROM orders")

    conn.commit()
    conn.close()
clear_db()