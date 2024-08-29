from fastapi import status
from fastapi.testclient import TestClient


def test_read_root(client: TestClient) -> None:
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK


def test_read_item(client: TestClient) -> None:
    response = client.get("/items/1")

    assert response.status_code == status.HTTP_200_OK
