import requests

def test_post_orders(clear_db):

    post_data = {
        "name": "TestUser",
        "email": "test_user@example.com",
        "address": "TestAddress",
        "product": "TestProduct",
        "quantity": 2
    }

    response = requests.post("http://127.0.0.1:5000/api/order", json=post_data)
    assert response.status_code == 201
    
    response = requests.get("http://127.0.0.1:5000/orders")
    assert response.status_code == 200
    orders = response.json()
    for order in orders:
        assert "id" in order
        assert "name" in order
        assert "email" in order
        assert "address" in order
        assert "product" in order
        assert "quantity" in order
    
    assert any(
    order["name"] == "TestUser" and 
    order["email"] == "test_user@example.com" and
    order["address"] == "TestAddress" and 
    order["product"] == "TestProduct" and
    order["quantity"] == 2
    for order in orders
    )

    for order in orders:
        assert isinstance(order["id"], int)
        assert isinstance(order["name"], str)
        assert isinstance(order["email"], str)
        assert isinstance(order["address"], str)
        assert isinstance(order["product"], str)
        assert isinstance(order["quantity"], int)
