from tests.helpers.db_utils import get_order_from_db

def test_put_order(client):
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

    # DB check - CREATE
    row = get_order_from_db(order_id)

    assert row is not None
    assert row.name == "User"
    assert row.email == "user@example.com"
    assert row.address == "Address"
    assert row.product == "Product"
    assert row.quantity == 2

    # ==================================================
    # ACT - PUT
    # ==================================================
    put_data = {
        "name": "PutUser",
        "email": "put_user@example.com",
        "address": "PutAddress",
        "product": "PutProduct",
        "quantity": 6
    }

    res = client.put(f"/api/order/{order_id}", json=put_data)

    assert res.status_code == 200
    assert res.get_json()["message"] == "order updated"

    # ==================================================
    # ASSERT - PUT (API)
    # ==================================================
    res = client.get(f"/api/order/{order_id}")

    assert res.status_code == 200

    updated = res.get_json()

    assert updated["name"] == "PutUser"
    assert updated["email"] == "put_user@example.com"
    assert updated["address"] == "PutAddress"
    assert updated["product"] == "PutProduct"
    assert updated["quantity"] == 6

    # ==================================================
    # ASSERT - PUT (DB)
    # ==================================================
    row = get_order_from_db(order_id)

    assert row is not None
    assert row.name == "PutUser"
    assert row.email == "put_user@example.com"
    assert row.address == "PutAddress"
    assert row.product == "PutProduct"
    assert row.quantity == 6