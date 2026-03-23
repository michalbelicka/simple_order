import sqlite3
import os

def get_order_from_db(order_id):
    db_path = os.path.join(os.path.dirname(__file__ ), "..", "..", "orders.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id, ))
    row = cursor.fetchone()

    conn.close()
    return row
    