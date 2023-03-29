import pytest


valid_post_requests = [
        {
            'device_id': 'test_1',
            'latitude': -10.123,
            'longitude': 23.12,
            'time': 12312321
        },
        {
            'device_id': 'test_2',
            'latitude': -90,
            'longitude': 180.0,
            'time': 1532153215312351235,
            'accuracy': 10,
            'speed': 3.4,
            'speed_accuracy': 9992.3123
        },
        {
            'device_id': 'test_3',
            'latitude': 90.0,
            'longitude': -180,
            'time': 229213218888282,
            'speed': 0.0023,
            'speed_accuracy': None,
            'user_id': 'Adamy',
            'boat_class': 'Laser'
        },
        {
            'device_id': 'test_4',
            'latitude': 10.333123,
            'longitude': 112.1,
            'time': 2,
            'accuracy': None,
            'user_id': None,
            'boat_class': None
        }
    ]


@pytest.fixture(params=valid_post_requests)
def valid_post(request):
    return request.param


invalid_post_requests = [
    {'device_id': 'adamy', 'latitude': -10.123, 'longitude': 111.222},
    {'latitude': -10.123, 'longitude': 111.22, 'time': 23.11},
    {'latitude': None, 'longitude': None, 'time': None}
]


@pytest.fixture(params=invalid_post_requests)
def invalid_post(request):
    return request.param
