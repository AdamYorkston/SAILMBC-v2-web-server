import pytest
import requests
from typing import Any


valid_post_requests = [
    {'user_id': 'adamy',
     'latitude': -10.123,
     'longitude': 23.12,
     'time': 123300003},
    {'user_id': 'HelloThere',
     'latitude': -90,
     'longitude': 180.0,
     'time': 33.22,
     'accuracy': 10,
     'speed': 3.4,
     'speed_accuracy': 9992.3123},
    {'user_id': '12331',
     'latitude': 90.0,
     'longitude': -180,
     'time': 1233301232132000,
     'speed': 0.0023,
     'speed_accuracy': None},
    {'user_id': '@]2[}]',
     'latitude': 10.333123,
     'longitude': 112.1,
     'time': 1233.33232,
     'accuracy': None}
]


invalid_post_requests = [
    {'user_id': 'adamy', 'latitude': -10.123, 'longitude': 111.222},
    {'latitude': -10.123, 'longitude': 111.22, 'time': 23.11},
    {'latitude': None, 'longitude': None, 'time': None}
]


@pytest.mark.parametrize("post_data", invalid_post_requests)
def test_invalid_request(post_data: Any):
    r = requests.post('http://localhost:80/post-data', json=post_data)
    assert r.status_code == 400


@pytest.mark.parametrize("sample_post", valid_post_requests)
def test_valid_request(sample_post: dict[str, Any]):
    r = requests.post('http://localhost:80/post-data', json=sample_post)
    assert r.status_code == 200
