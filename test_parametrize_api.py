import pytest
import requests

test_data = [
    (
        {"name": "Tester", "email": "tester@example.com", "address":      "TestAddress", "product": "computer", "quantity": 1},
        {"name": "Tester", "email": "tester@example.com", "address": "TestAddress", "product": "computer", "quantity": 1},
        201
    ),
    (
        {"name": "John", "email": "john@example.com", "address": "Bratislava", "product": "notebook", "quantity": 3},
        {"name": "John", "email": "john@example.com", "address": "Bratislava", "product": "notebook", "quantity": 3},
        201
    ),
    (
        {"name": "", "email": "", "address": "", "product": "", "quantity": 0},
        {},
        400
    ),
    (
        {"name": "Anna", "email": "anna@example.com", "address": "Trnava", "product": "", "quantity": 3},
        {},
        400
    )
]
@pytest.mark.parametrize("payload, expected_payload, expected_status", test_data)
def test_post_api_order(clear_db, payload, expected_payload, expected_status):

    post_response = requests.post("http://127.0.0.1:5000/api/order", json=payload)
    assert post_response.status_code == expected_status
    
    if expected_status == 201:
        get_response = requests.get("http://127.0.0.1:5000/orders")
        order = get_response.json()
        assert get_response.status_code == 200
        assert all(order[-1][key] == value for key, value in expected_payload.items())
        