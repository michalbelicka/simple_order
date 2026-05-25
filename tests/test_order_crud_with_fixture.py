import requests
import pytest
from tests.helpers.db_utils import get_order_from_db

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


def test_created_order_saved_in_db(created_order):
    order_id = created_order

    row = get_order_from_db(order_id)
    assert row is not None

    assert row.name == "TestUser"
    assert row.email == "test_user@example.com"
    assert row.address == "TestAddress"
    assert row.product == "TestProduct"
    assert row.quantity == 2
    
    assert isinstance(row.id, int)
    assert isinstance(row.name, str)
    assert isinstance(row.email, str)
    assert isinstance(row.address, str)
    assert isinstance(row.product, str)
    assert isinstance(row.quantity, int)


# GET TEST API
def test_get_order_by_id(created_order):
    order_id = created_order
    response = requests.get(f"http://127.0.0.1:5000/api/order/{order_id}")
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
    

# PUT TEST API
def test_put_order_by_id(created_order):
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

    response_get = requests.get(f"http://127.0.0.1:5000/api/order/{order_id}")
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


def test_updated_order_saved_in_db(created_order):
    order_id = created_order

    row = get_order_from_db(order_id)
    assert row is not None

    assert row.name == "UpdatedUser"
    assert row.email == "Updated_user@example.com"
    assert row.address == "UpdatedAddress"
    assert row.product == "UpdatedProduct"
    assert row.quantity == 4

    assert isinstance(row.id, int)
    assert isinstance(row.name, str)
    assert isinstance(row.email, str)
    assert isinstance(row.address, str)
    assert isinstance(row.product, str)
    assert isinstance(row.quantity, int)


# PATCH TEST API
def test_patch_order_by_id(created_order):
    order_id = created_order
    patch_data = {
        "quantity": 5
    }
    response_patch = requests.patch(f"http://127.0.0.1:5000/api/order/{order_id}", json=patch_data)
    assert response_patch.status_code == 200
    assert response_patch.json()["message"] == "Order updated successfully"

    patch_order = requests.get(f"http://127.0.0.1:5000/api/order/{order_id}").json()

    assert patch_order["quantity"] == 5
    assert patch_order["name"] == "UpdatedUser"
    assert patch_order["email"] == "Updated_user@example.com"
    assert patch_order["address"] == "UpdatedAddress"
    assert patch_order["product"] == "UpdatedProduct"

    assert isinstance(patch_order["id"], int)
    assert isinstance(patch_order["quantity"], int)
    assert isinstance(patch_order["name"], str)
    assert isinstance(patch_order["email"], str)
    assert isinstance(patch_order["address"], str)
    assert isinstance(patch_order["product"], str)


def test_patched_order_saved_in_db(created_order):
    order_id = created_order

    row = get_order_from_db(order_id)
    assert row is not None

    assert row.quantity == 5
    assert row.name == "UpdatedUser"
    assert row.email == "Updated_user@example.com"
    assert row.address == "UpdatedAddress"
    assert row.product == "UpdatedProduct"

    assert isinstance(row.id, int)
    assert isinstance(row.quantity, int)
    assert isinstance(row.name, str)
    assert isinstance(row.email, str)
    assert isinstance(row.address, str)
    assert isinstance(row.product, str)


# DELETE TEST API
def test_delete_order_by_id(created_order):
    order_id = created_order
    response_del = requests.delete(f"http://127.0.0.1:5000/api/order/{order_id}")
    assert response_del.status_code == 200
    assert response_del.json()["message"] == "Order successfully deleted"
    response_get = requests.get(f"http://127.0.0.1:5000/api/order/{order_id}")
    assert response_get.status_code == 404


def test_deleted_order_removed_from_db(created_order):
    order_id = created_order
    row = get_order_from_db(order_id)

    assert row is None