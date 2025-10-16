import requests
from test_post_fixture import created_order

def test_update_order(created_order):
    order_id = created_order

    update_data = {
        "name": "UpdatedUser",
        "email": "Updated_user@example.com",
        "address": "UpdatedAddress",
        "product": "UpdatedProduct",
        "quantity": 4
    }

    response = requests.put(f"http://127.0.0.1:5000/api/order/{order_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["message"] == "order updated"

    response_get = requests.get(f"http://127.0.0.1:5000/order/{order_id}")
    updated_order = response_get.json()

    
    assert updated_order["name"] == "UpdatedUser"
    assert updated_order["email"] == "Updated_user@example.com"
    assert updated_order["address"] == "UpdatedAddress"
    assert updated_order["product"] == "UpdatedProduct"
    assert updated_order["quantity"] == 4

    assert isinstance(updated_order["id"], int)
    assert isinstance(updated_order["name"], str)
    assert isinstance(updated_order["email"], str)
    assert isinstance(updated_order["address"], str)
    assert isinstance(updated_order["product"], str)
    assert isinstance(updated_order["quantity"], int)