from flask import Flask, render_template, request, jsonify
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR / "orders.db"

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route("/")
def index():
    return render_template("order_form.html")

# Create new order with ID (html)
@app.route("/order", methods=["POST"])
def order():

    name = request.form.get("name")
    email = request.form.get("email")
    address = request.form.get("address")
    product = request.form.get("product")
    quantity = request.form.get("quantity")

    if not (name and email and address and product and quantity):
        return "Chýbajú povinné údaje", 400
    
    new_order = Order(
        name=name,
        email=email,
        address=address,
        product=product,
        quantity=quantity
    )

    db.session.add(new_order)
    db.session.commit()
    
    # conn = sqlite3.connect("orders.db")
    # c = conn.cursor()
    # c.execute(
    #     "INSERT INTO orders (name, email, address, product, quantity)"
    #     "VALUES (?, ?, ?, ?, ?)",
    #     (name, email, address, product, quantity)
    # )
    # conn.commit()
    # order_id = c.lastrowid
    # conn.close()
    return render_template("success.html", order_id=new_order.id)

# Create new order with ID (API)
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
    
    new_order = Order(
        name=name,
        email=email,
        address=address,
        product=product,
        quantity=quantity
    )
    db.session.add(new_order)
    db.session.commit()

    return jsonify({
        "message": "Order created",
        "id": new_order.id
    }), 201

# GET all orders (API)
@app.route("/api/orders", methods=["GET"])
def get_orders():
   
    orders = Order.query.all()

    result = []

    for order in orders:
        result.append({
            "id": order.id,
            "name": order.name,
            "email": order.email,
            "address": order.address,
            "product": order.product,
            "quantity": order.quantity
        })

    return jsonify(result), 200

# GET order with ID (API)
@app.route("/api/order/<int:order_id>", methods=["GET"])
def get_order_by_id(order_id):
   
    order = db.session.get(Order, order_id)

    if order:
        return jsonify({
            "id": order.id,
            "name": order.name,
            "email": order.email,
            "address": order.address,
            "product": order.product,
            "quantity": order.quantity
        }), 200
    
    return jsonify({"error": "Order not found"}), 404

# PUT order with ID (API)
@app.route("/api/order/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    data = request.get_json() or {}

    name = data.get("name")
    email = data.get("email")
    address = data.get("address")
    product = data.get("product")
    quantity = data.get("quantity")

    if not (name and email and address and product and quantity):
        return jsonify({"error": "Missing data - all fields required for PUT"}), 400
    
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute(
        "UPDATE orders SET name=?, email=?, address=?, product=?, quantity=? WHERE id=?",
        (name, email, address, product, quantity, order_id)
    )
    conn.commit()
    
    if c.rowcount == 0:
        conn.close()
        return jsonify({"error": "order not found"}), 404
    
    conn.close()
    return jsonify({"message": "order updated"}), 200

# PATCH order with ID (API)
@app.route("/api/order/<int:order_id>", methods=["PATCH"])
def patch_order(order_id):
    data = request.get_json() or {}

    name = data.get("name")
    email = data.get("email")
    address = data.get("address")
    product = data.get("product")
    quantity = data.get("quantity")

    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()

    if name:
        c.execute("UPDATE orders SET name=? WHERE id=?", (name, order_id))
    if email:
        c.execute("UPDATE orders SET email=? WHERE id=?", (email, order_id))
    if address:
        c.execute("UPDATE orders SET address=? WHERE id=?", (address, order_id))
    if product:
        c.execute("UPDATE orders SET product=? WHERE id=?", (product, order_id))
    if quantity:
        c.execute("UPDATE orders SET quantity=? WHERE id=?", (quantity, order_id))
    
    conn.commit()
    conn.close()
    return jsonify({"message": "Order updated successfully"}), 200

# DELETE order by ID (API)
@app.route("/api/order/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("DELETE FROM orders WHERE id=?", (order_id,))
    conn.commit()

    if c.rowcount == 0:
        conn.close()
        return jsonify({"error": "Order not found"}), 404
    
    conn.close()
    return jsonify({"message": "Order successfully deleted"}), 200
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)