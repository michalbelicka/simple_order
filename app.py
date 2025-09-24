from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("order_form.html")

@app.route("/order", methods=["POST"])
def order():
    name = request.form.get("name")
    email = request.form.get("email")
    address = request.form.get("address")
    product = request.form.get("product")
    quantity = request.form.get("quantity")

    if not (name and email and address and product and quantity):
        return "Chýbajú povinné údaje", 400
    
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO orders (name, email, address, product, quantity)"
        "VALUES (?, ?, ?, ?, ?)",
        (name, email, address, product, quantity)
    )
    conn.commit()
    conn.close()

    return render_template("success.html")

@app.route("/orders", methods=["GET"])
def get_orders():
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("SELECT name, email, address, product, quantity FROM orders")
    rows = c.fetchall()
    orders = [
        {
             "name": row[0],
             "email": row[1],
             "address": row[2],
             "product": row[3],
             "quantity": row[4]
        }
        for row in rows
    ]
    return jsonify(orders)

app.run(debug=True)