from tests.helpers.db_utils import get_order_from_db

def test_get_order(client):
    # ==================================================
    # ARRANGE - CREATE
    # ==================================================
    post_data = {
        "name": "User",
        "email": "user@example.com",
        "address": "Address",
        "product": "Product",
        "quantity": 2
    }

    res = client.post("/api/order", json=post_data)

    assert res.status_code == 201

    order_id = res.get_json()["id"]

    # ==================================================
    # ACT - GET
    # ==================================================
    res = client.get(f"/api/order/{order_id}")

    # ==================================================
    # ASSERT - GET (API)
    # ==================================================
    assert res.status_code == 200

    order = res.get_json()

    assert order["name"] == "User"
    assert order["email"] == "user@example.com"
    assert order["address"] == "Address"
    assert order["product"] == "Product"
    assert order["quantity"] == 2

    # ==================================================
    # ASSERT - GET (DB)
    # ==================================================
    row = get_order_from_db(order_id)

    assert row is not None
    assert row.name == "User"
    assert row.email == "user@example.com"
    assert row.address == "Address"
    assert row.product == "Product"
    assert row.quantity == 2