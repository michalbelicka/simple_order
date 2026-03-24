import pytest
import requests
from tests.helpers.db_utils import get_order_from_db

@pytest.fixture(scope="module")
def new_order(clear_db):

    post_data = {
        "name": "User2",
        "email": "user2@example.com",
        "address": "Address2",
        "product": "Product2",
        "quantity": 3
    }

    response = requests.post("http://127.0.0.1:5000/api/order", json=post_data)

    assert response.status_code == 201
    assert response.json()["message"] == "Order created"

    order_id = response.json()["id"]

    response_get = requests.get(f"http://127.0.0.1:5000/api/order/{order_id}")
    order = response_get.json()

    assert order["name"] == "User2"
    assert order["email"] == "user2@example.com"
    assert order["address"] == "Address2"
    assert order["product"] == "Product2"
    assert order["quantity"] == 3

    assert isinstance(order["id"], int)
    assert isinstance(order["name"], str)
    assert isinstance(order["email"], str)
    assert isinstance(order["address"], str)
    assert isinstance(order["product"], str)
    assert isinstance(order["quantity"], int)

    yield order_id

    response_del = requests.delete(f"http://127.0.0.1:5000/api/order/{order_id}")

    assert response_del.status_code == 200
    assert response_del.json()["message"] == "Order successfully deleted"

def test_order_saved_in_db(new_order):

    order_id = new_order

    row = get_order_from_db(order_id)
    assert row is not None

    assert row["name"] == "User2"
    assert row["email"] == "user2@example.com"
    assert row["address"] == "Address2"
    assert row["product"] == "Product2"
    assert row["quantity"] == 3
    
    assert isinstance(row["id"], int)
    assert isinstance(row["name"], str)
    assert isinstance(row["email"], str)
    assert isinstance(row["address"], str)
    assert isinstance(row["product"], str)
    assert isinstance(row["quantity"], int)


def test_patch_order(new_order):

    order_id = new_order

    patch_data = {
        "name": "User5"
    }

    response_patch = requests.patch(f"http://127.0.0.1:5000/api/order/{order_id}", json=patch_data)

    assert response_patch.status_code == 200
    assert response_patch.json()["message"] == "Order updated successfully"
    
    response_get = requests.get(f"http://127.0.0.1:5000/api/order/{order_id}")
    assert response_get.status_code == 200
    updated_order = response_get.json()

    assert updated_order["name"] == "User5"
    assert updated_order["email"] == "user2@example.com"
    assert updated_order["address"] == "Address2"
    assert updated_order["product"] == "Product2"
    assert updated_order["quantity"] == 3

    assert isinstance(updated_order["id"], int)
    assert isinstance(updated_order["name"], str)
    assert isinstance(updated_order["email"], str)
    assert isinstance(updated_order["address"], str)
    assert isinstance(updated_order["product"], str)
    assert isinstance(updated_order["quantity"], int)

    
def test_patched_order_saved_in_db(new_order):

    order_id = new_order

    row = get_order_from_db(order_id)
    assert row is not None

    assert row["name"] == "User5"
    assert row["email"] == "user2@example.com"
    assert row["address"] == "Address2"
    assert row["product"] == "Product2"
    assert row["quantity"] == 3
    
    assert isinstance(row["id"], int)
    assert isinstance(row["name"], str)
    assert isinstance(row["email"], str)
    assert isinstance(row["address"], str)
    assert isinstance(row["product"], str)
    assert isinstance(row["quantity"], int)

