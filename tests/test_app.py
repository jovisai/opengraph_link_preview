import pytest
from flask import json

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        # Give control to your test
        yield client


def test_health_of_link_service(client):
    rv = client.get("/are_you_alive")
    assert "Hello from Link service" == json.loads(rv.data)['message']


def test_bad_non_existing_api(client):
    rv = client.get("/not_there")
    assert rv.status_code == 404


# test blueprints
def test_link_service_good_url(client):
    data = {
        "link": "https://en.wikipedia.org/wiki/Under_the_Seas"
    }
    response = client.post("/v1/", json=data)
    assert response.content_type == 'application/json'
    assert json.loads(response.data)['url'] == data['link']
    assert response.status_code == 200


def test_link_service_bad_url(client):
    data = {
        "link": "https://docs.docker.com/xyz"
    }
    response = client.post("/v1/", json=data)
    assert response.status_code == 500
    assert json.loads(response.data)[
               'message'] == "something went wrong in the parsing, please check the url again if it exists"
