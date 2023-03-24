import requests


def test_flask_health_check():
    r = requests.get('http://localhost:80/flask-health-check')
    assert r.status_code == 200
