import requests
from typing import Any


def test_invalid_request(invalid_post: Any):
    r = requests.post('http://localhost:80/post-data', json=invalid_post)
    assert r.status_code == 400


def test_valid_request(valid_post: dict[str, Any]):
    r = requests.post('http://localhost:80/post-data', json=valid_post)
    assert r.status_code == 200
