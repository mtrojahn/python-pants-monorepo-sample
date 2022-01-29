# this is a fix so requests is found during tests
import requests  # noqa

from fastapi.testclient import TestClient
from webservices.converter_api.app import app

client = TestClient(app)


def test_get_string():
    response = client.get("/?number=1")
    assert response.status_code == 200
    assert response.json() == {"message": "1"}
