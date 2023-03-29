import requests
from typing import Any
import time


def test_valid_request(valid_post: dict[str, Any]):

    request_time = int(time.time())
    requests.post('http://localhost:80/post-data',
                  json=valid_post)

    r = requests.get('http://localhost:80/get-data',
                     json={'min_time': request_time})

    data = [d for d in r.json()['data']
            if d['device_id'] == valid_post['device_id']]

    assert len(data) == 1

    returned_post = data[-1]
    for key in valid_post.keys():
        assert valid_post[key] == returned_post[key]
