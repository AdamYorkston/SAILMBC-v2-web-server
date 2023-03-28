import pytest
import requests
import time

valid_get_requests = [
    {},
    {'min_time': 100},
    {'min_time': time.time()}
]

invalid_get_requests = [
    {'time_from': 100},
    {'min_time': -12},
    {'min_time': '12:30'}
]


@pytest.mark.parametrize("get_data", valid_get_requests)
def test_valid_request(get_data: dict):
    r = requests.get('http://localhost:80/get-data', json=get_data)
    assert r.status_code == 200


@pytest.mark.parametrize("get_data", invalid_get_requests)
def test_invalid_request(get_data: dict):
    r = requests.get('http://localhost:80/get-data', json=get_data)
    assert r.status_code == 400
