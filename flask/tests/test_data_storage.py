import pytest
import requests
from typing import Any

request_time = 1679691986

post_requests = [
    {'device_id': 'adamy',
     'latitude': -10.123,
     'longitude': 23.12,
     'time': request_time},
    {'device_id': 'HelloThere',
     'latitude': -90,
     'longitude': 180.0,
     'time': request_time,
     'accuracy': 10,
     'speed': 3.4,
     'speed_accuracy': 9992.3123},
    {'device_id': '12331',
     'latitude': 90.0,
     'longitude': -180,
     'time': request_time,
     'speed': 0.0023,
     'speed_accuracy': None,
     'user_id': 'Adamy',
     'boat_class': 'Laser'},
    {'device_id': '@]2[}]',
     'latitude': 10.333123,
     'longitude': 112.1,
     'time': request_time,
     'accuracy': None,
     'user_id': None,
     'boat_class': None}
]


@pytest.mark.parametrize("sample_post", post_requests)
def test_valid_request(sample_post: dict[str, Any]):
    requests.post('http://localhost:80/post-data',
                  json=sample_post)
    r = requests.get('http://localhost:80/get-data',
                     json={'from_time': request_time-1})
    assert any([sample_post == d for d in r.json()['data']])
