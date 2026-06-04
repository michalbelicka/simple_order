from tests.helpers.db_utils import get_order_from_db

def test_order_crud_lifecycle(client):
    # ==================================================
    # CREATE - POST
    # ==================================================
    post_data = {
        "name": "TestUser",
        "email": "test_user@example.com",
        "address": "TestAddress",
        "product": "TestProduct",
        "quantity": 2
    }

    res = client.post("/api/order", json=post_data)

    assert res.status_code == 201

    order_id = res.get_json()["id"]

    # DB check - CREATE
    row = get_order_from_db(order_id)

    assert row is not None
    assert row.name == "TestUser"
    assert row.email == "test_user@example.com"
    assert row.address == "TestAddress"
    assert row.product == "TestProduct"
    assert row.quantity == 2

    # ==================================================
    # READ - GET
    # ==================================================
    res = client.get(f"/api/order/{order_id}")

    assert res.status_code == 200

    order = res.get_json()

    assert order["name"] == "TestUser"
    assert order["email"] == "test_user@example.com"
    assert order["address"] == "TestAddress"
    assert order["product"] == "TestProduct"
    assert order["quantity"] == 2

    # ==================================================
    # UPDATE - PUT
    # ==================================================
    put_data = {
        "name": "UpdatedUser",
        "email": "updated_user@example.com",
        "address": "UpdatedAddress",
        "product": "UpdatedProduct",
        "quantity": 4
    }

    res = client.put(f"/api/order/{order_id}", json=put_data)

    assert res.status_code == 200
    assert res.get_json()["message"] == "order updated"

    # API check - PUT
    res = client.get(f"/api/order/{order_id}")

    updated = res.get_json()

    assert updated["name"] == "UpdatedUser"
    assert updated["email"] == "updated_user@example.com"
    assert updated["address"] == "UpdatedAddress"
    assert updated["product"] == "UpdatedProduct"
    assert updated["quantity"] == 4

    # DB check - PUT
    row = get_order_from_db(order_id)

    assert row is not None
    assert row.name == "UpdatedUser"
    assert row.email == "updated_user@example.com"
    assert row.address == "UpdatedAddress"
    assert row.product == "UpdatedProduct"
    assert row.quantity == 4

    # ==================================================
    # PARTIAL UPDATE - PATCH
    # ==================================================
    patch_data = {
        "quantity": 5
    }

    res = client.patch(f"/api/order/{order_id}", json=patch_data)

    assert res.status_code == 200
    assert res.get_json()["message"] == "Order updated successfully"

    # API check - PATCH
    res = client.get(f"/api/order/{order_id}")

    patched = res.get_json()

    assert patched["quantity"] == 5
    assert patched["name"] == "UpdatedUser"
    assert patched["email"] == "updated_user@example.com"
    assert patched["address"] == "UpdatedAddress"
    assert patched["product"] == "UpdatedProduct"

    # DB check - PATCH
    row = get_order_from_db(order_id)

    assert row is not None
    assert row.quantity == 5
    assert row.name == "UpdatedUser"
    assert row.email == "updated_user@example.com"
    assert row.address == "UpdatedAddress"
    assert row.product == "UpdatedProduct"

    # ==================================================
    # DELETE
    # ==================================================
    res = client.delete(f"/api/order/{order_id}")

    assert res.status_code == 200
    assert res.get_json()["message"] == "Order successfully deleted"

    # API check - DELETE
    res = client.get(f"/api/order/{order_id}")

    assert res.status_code == 404
    assert res.get_json()["error"] == "Order not found"

    # DB check - DELETE
    row = get_order_from_db(order_id)

    assert row is None