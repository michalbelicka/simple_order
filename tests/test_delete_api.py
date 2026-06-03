from tests.helpers.db_utils import get_order_from_db

def test_delete_order(client):
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
    # ACT - DELETE
    # ==================================================
    res = client.delete(f"/api/order/{order_id}")

    # ==================================================
    # ASSERT - DELETE (API)
    # ==================================================
    assert res.status_code == 200
    assert res.get_json()["message"] == "Order successfully deleted"

    res = client.get(f"/api/order/{order_id}")

    assert res.status_code == 404
    assert res.get_json()["error"] == "Order not found"

    # ==================================================
    # ASSERT - DELETE (DB)
    # ==================================================
    row = get_order_from_db(order_id)

    assert row is None