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

@app.route("/api/order", methods=["POST"])
def get_api_order():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    address = data.get("address")
    product = data.get("product")
    quantity = data.get("quantity")

    if not (name and email and address and product and quantity):
        return jsonify({"error": "Missing data"}), 400
    
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO orders (name, email, address, product, quantity)"
        "VALUES (?, ?, ?, ?, ?)",
        (name, email, address, product, quantity)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Order created"}), 201

@app.route("/orders", methods=["GET"])
def get_orders():
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("SELECT id, name, email, address, product, quantity FROM orders")
    rows = c.fetchall()
    orders = [
        {
             "id": row[0],
             "name": row[1],
             "email": row[2],
             "address": row[3],
             "product": row[4],
             "quantity": row[5]
        }
        for row in rows
    ]
    return jsonify(orders), 200

app.run(debug=True)