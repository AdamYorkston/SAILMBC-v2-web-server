import requests
import pytest
from types import MethodType
from app import create_app


class DockerClient():
    """
    creates a client that mimics app.test_client() get and post methods.
    this allows us to use the same unit tests for both local and
    dockerised versions of the app
    """
    url_template = "http://localhost:80{path}"

    def get(self, path, *args, **kwargs):
        r = requests.get(self.url_template.format(path=path), *args, **kwargs)
        r.get_json = MethodType(lambda r: r.json(), r)
        return r

    def post(self, path, *args, **kwargs):
        r = requests.post(self.url_template.format(path=path), *args, **kwargs)
        r.get_json = MethodType(lambda r: r.json(), r)
        return r


test_client = create_app(local=True).test_client()
docker_client = DockerClient()


@pytest.fixture(params=['flask-server', 'docker-server'])
def client(request):
    if request.param == 'flask-server':
        return test_client
    elif request.param == 'docker-server':
        return docker_client
