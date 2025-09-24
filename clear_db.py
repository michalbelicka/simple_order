import sqlite3

conn = sqlite3.connect("orders.db")
c = conn.cursor()
c.execute("DELETE FROM orders")

conn.commit()
conn.close()