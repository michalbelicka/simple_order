from flask import Flask, render_template, request, jsonify
import os
from models import db, Order

app = Flask(__name__)

db_url = os.getenv("DATABASE_URL")

if not db_url:
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

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

    order = db.session.get(Order, order_id)

    if not order:
        return jsonify({"error": "Order not found"}), 404

    name = data.get("name")
    email = data.get("email")
    address = data.get("address")
    product = data.get("product")
    quantity = data.get("quantity")

    if not (name and email and address and product and quantity):
        return jsonify({"error": "Missing data - all fields required for PUT"}), 400
    
    order.name = name
    order.email = email
    order.address = address
    order.product = product
    order.quantity = quantity

    db.session.commit()
    
    return jsonify({"message": "order updated"}), 200

# PATCH order with ID (API)
@app.route("/api/order/<int:order_id>", methods=["PATCH"])
def patch_order(order_id):

    data = request.get_json() or {}

    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    order = db.session.get(Order, order_id)

    if not order:
        return jsonify({"error": "Order not found"}), 404
    
    if "name" in data:
        order.name = data["name"]

    if "email" in data:
        order.email = data["email"]

    if "address" in data:
        order.address = data["address"]

    if "product" in data:
        order.product = data["product"]

    if "quantity" in data:
        order.quantity = data["quantity"]

    db.session.commit()
    
    return jsonify({"message": "Order updated successfully"}), 200

# DELETE order by ID (API)
@app.route("/api/order/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
 
    order = db.session.get(Order, order_id)

    if not order:
        return jsonify({"error": "Order not found"}), 404
    
    db.session.delete(order)
    db.session.commit()
    
    return jsonify({"message": "Order successfully deleted"}), 200

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)