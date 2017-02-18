import pytest
from {{cookiecutter.package_name}} import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def app_client(app):
    client = app.test_client()
    return client


def test_index_endpoint(client):
    index_response = client.get('/')

    assert index_response.json == {
        'message': 'Hello world!'
    }

    assert index_response.status_code == 200
