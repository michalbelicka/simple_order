import requests
import pytest

@pytest.fixture()
def created_order(clear_db):

    post_data = {
        "name": "TestUser",
        "email": "test_user@example.com",
        "address": "TestAddress",
        "product": "TestProduct",
        "quantity": 2
    }

    response = requests.post("http://127.0.0.1:5000/api/order", json=post_data)
    assert response.status_code == 201
    assert response.json()["message"] == "Order created"
    order_id = response.json()["id"]
    assert isinstance(order_id, int)
    return order_id

def test_get_order_by_id(created_order):
    order_id = created_order
    response = requests.get(f"http://127.0.0.1:5000/order/{order_id}")
    assert response.status_code == 200
    order = response.json()

    assert order["name"] == "TestUser" 
    assert order["email"] == "test_user@example.com" 
    assert order["address"] == "TestAddress"
    assert order["product"] == "TestProduct"
    assert order["quantity"] == 2
    
    assert isinstance(order["id"], int)
    assert isinstance(order["name"], str)
    assert isinstance(order["email"], str)
    assert isinstance(order["address"], str)
    assert isinstance(order["product"], str)
    assert isinstance(order["quantity"], int)    
    