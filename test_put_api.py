import requests
from test_post_get_api_orders import test_created_order

def test_update_order(test_created_order):
    order_id = test_created_order

    update_data = {
        "name": "UpdatedUser",
        "email": "Updated_user@example.com",
        "address": "UpdatedAddress",
        "product": "UpdatedProduct",
        "quantity": 4
    }

    response = requests.put(f"http://127.0.0.1:5000/api/order/{order_id}", json=update_data)
    assert response.status_code == 200
    response_get = requests.get("http://127.0.0.1:5000/orders")
    updated_orders = response_get.json()

    for order in updated_orders:
        assert "id" in order
        assert "name" in order
        assert "email" in order
        assert "address" in order
        assert "product" in order
        assert "quantity" in order
    
    assert any(
    order["name"] == "UpdatedUser" and 
    order["email"] == "Updated_user@example.com" and
    order["address"] == "UpdatedAddress" and 
    order["product"] == "UpdatedProduct" and
    order["quantity"] == 4
    for order in updated_orders
    )

    for order in updated_orders:
        assert isinstance(order["id"], int)
        assert isinstance(order["name"], str)
        assert isinstance(order["email"], str)
        assert isinstance(order["address"], str)
        assert isinstance(order["product"], str)
        assert isinstance(order["quantity"], int)