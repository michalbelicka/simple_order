# import requests
# from test_post_fixture import created_order

# def test_patch_order(created_order):
#     order_id = created_order

#     patch_data = {
#         "quantity": 5
#     }
#     response = requests.patch(f"http://127.0.0.1:5000/api/order/{order_id}", json=patch_data)
#     assert response.status_code == 200
#     assert response.json()["message"] == "Order updated successfully"

#     updated_order = requests.get(f"http://127.0.0.1:5000/order/{order_id}").json()

#     assert updated_order["quantity"] == 5
#     assert isinstance(updated_order["quantity"], int)

#     assert updated_order["name"] == "UpdatedUser"
#     assert isinstance(updated_order["name"], str)