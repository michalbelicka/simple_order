from tests.helpers.db_utils import get_order_from_db

def test_patch_order(client):
    # ==================================================
    # ARRANGE - CREATE
    # ==================================================
    post_data = {
        "name": "User2",
        "email": "user2@example.com",
        "address": "Address2",
        "product": "Product2",
        "quantity": 3
    }

    res = client.post("/api/order", json=post_data)
    assert res.status_code == 201
    order_id = res.get_json()["id"]

    # DB check - CREATE
    row = get_order_from_db(order_id)
    assert row is not None
    assert row.name == "User2"
    assert row.email == "user2@example.com"

    # ==================================================
    # ACT - PATCH
    # ==================================================
    patch_data = {"name": "User5"}

    res = client.patch(f"/api/order/{order_id}", json=patch_data)
    assert res.status_code == 200
    assert res.get_json()["message"] == "Order updated successfully"

    # ==================================================
    # ASSERT - PATCH (API)
    # ==================================================
    res = client.get(f"/api/order/{order_id}")
    assert res.status_code == 200

    updated = res.get_json()
    assert updated["name"] == "User5"
    assert updated["email"] == "user2@example.com"

    # ==================================================
    # ASSERT - PATCH (DB)
    # ==================================================
    row = get_order_from_db(order_id)
    assert row is not None
    assert row.name == "User5"
    assert row.email == "user2@example.com"