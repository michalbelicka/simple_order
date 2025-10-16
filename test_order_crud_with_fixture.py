import requests
import pytest

@pytest.fixture(scope="module")
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

# GET TEST
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
    
# PUT TEST
def test_put_order(created_order):
    order_id = created_order
    update_data = {
        "name": "UpdatedUser",
        "email": "Updated_user@example.com",
        "address": "UpdatedAddress",
        "product": "UpdatedProduct",
        "quantity": 4
    }
    response_put = requests.put(f"http://127.0.0.1:5000/api/order/{order_id}", json=update_data)
    assert response_put.status_code == 200
    assert response_put.json()["message"] == "order updated"

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

# PATCH TEST
def test_patch_order(created_order):
    order_id = created_order
    patch_data = {
        "quantity": 5
    }
    response_patch = requests.patch(f"http://127.0.0.1:5000/api/order/{order_id}", json=patch_data)
    assert response_patch.status_code == 200
    assert response_patch.json()["message"] == "Order updated successfully"

    patch_order = requests.get(f"http://127.0.0.1:5000/order/{order_id}").json()

    assert patch_order["quantity"] == 5
    assert isinstance(patch_order["quantity"], int)

    assert patch_order["name"] == "UpdatedUser"
    assert isinstance(patch_order["name"], str)

    assert patch_order["email"] == "Updated_user@example.com"
    assert isinstance(patch_order["email"], str)

    assert patch_order["address"] == "UpdatedAddress"
    assert isinstance(patch_order["address"], str)

    assert patch_order["product"] == "UpdatedProduct"
    assert isinstance(patch_order["product"], str)
    assert isinstance(patch_order["id"], int)