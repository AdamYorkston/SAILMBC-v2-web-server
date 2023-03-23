import pytest

valid_get_requests = [
    {},
    {'from_time': 100},
    {'from_time': 100.223}
]

@pytest.mark.parametrize("get_data", valid_get_requests)
def test_valid_request(client, get_data: dict):
    r = client.get('/get-data', json=get_data)
    assert r.status_code == 200