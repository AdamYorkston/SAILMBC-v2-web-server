import pytest
import requests
from typing import Any
import time

request_time = int(time.time())

post_requests = [
    {'device_id': 'data_storage_test_1',
     'latitude': -10.123,
     'longitude': 23.12,
     'time': request_time},
    {'device_id': 'data_storage_test_2',
     'latitude': -90,
     'longitude': 180.0,
     'time': request_time,
     'accuracy': 10,
     'speed': 3.4,
     'speed_accuracy': 9992.3123},
    {'device_id': 'data_storage_test_3',
     'latitude': 90.0,
     'longitude': -180,
     'time': request_time,
     'speed': 0.0023,
     'speed_accuracy': None,
     'user_id': 'Adamy',
     'boat_class': 'Laser'},
    {'device_id': 'data_storage_test_4',
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
                     json={'min_time': request_time})
    data = [d for d in r.json()['data']
            if d['device_id'] == sample_post['device_id']]

    assert len(data) == 1

    returned_post = data[-1]
    for key in sample_post.keys():
        assert sample_post[key] == returned_post[key]
