import pytest
import requests
from tests.helpers.db_utils import get_order_from_db

@pytest.fixture(scope="module")
def new_order(clear_db):
    
    post_data = {
        "name": "User",
        "email": "user@example.com",
        "address": "Address",
        "product": "Product",
        "quantity": 2
    }

    response = requests.post("http://127.0.0.1:5000/api/order", json=post_data)

    assert response.status_code == 201
    assert response.json()["message"] == "Order created"

    order_id = response.json()["id"]

    response_get = requests.get(f"http://127.0.0.1:5000/api/order/{order_id}")

    order = response_get.json()

    assert order["name"] == "User"
    assert order["email"] == "user@example.com"
    assert order["address"] == "Address"
    assert order["product"] == "Product"
    assert order["quantity"] == 2

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

    assert row.name == "User"
    assert row.email == "user@example.com"
    assert row.address == "Address"
    assert row.product == "Product"
    assert row.quantity == 2
    
    assert isinstance(row.id, int)
    assert isinstance(row.name, str)
    assert isinstance(row.email, str)
    assert isinstance(row.address, str)
    assert isinstance(row.product, str)
    assert isinstance(row.quantity, int)


def test_put_order(new_order):

    order_id = new_order

    put_data = {
        "name": "PutUser",
        "email": "put_user@example.com",
        "address": "PutAddress",
        "product": "PutProduct",
        "quantity": 6
    }

    response_put = requests.put(f"http://127.0.0.1:5000/api/order/{order_id}", json=put_data)

    assert response_put.status_code == 200
    assert response_put.json()["message"] == "order updated"

    response_get = requests.get(f"http://127.0.0.1:5000/api/order/{order_id}")
    updated_order = response_get.json()

    assert updated_order["name"] == "PutUser"
    assert updated_order["email"] == "put_user@example.com"
    assert updated_order["address"] == "PutAddress"
    assert updated_order["product"] == "PutProduct"
    assert updated_order["quantity"] == 6

    assert isinstance(updated_order["id"], int)
    assert isinstance(updated_order["name"], str)
    assert isinstance(updated_order["email"], str)
    assert isinstance(updated_order["address"], str)
    assert isinstance(updated_order["product"], str)
    assert isinstance(updated_order["quantity"], int)


def test_put_order_saved_in_db(new_order):

    order_id = new_order

    row = get_order_from_db(order_id)
    assert row is not None

    assert row.name == "PutUser"
    assert row.email == "put_user@example.com"
    assert row.address == "PutAddress"
    assert row.product == "PutProduct"
    assert row.quantity == 6
    
    assert isinstance(row.id, int)
    assert isinstance(row.name, str)
    assert isinstance(row.email, str)
    assert isinstance(row.address, str)
    assert isinstance(row.product, str)
    assert isinstance(row.quantity, int)
