def test_flask_health_check(client):
    r = client.get('/flask-health-check')
    assert r.status_code == 200
