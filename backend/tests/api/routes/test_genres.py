from fastapi.testclient import TestClient
from sqlmodel import Session

from tests.utils.book.genre import create_random_genre
from tests.utils.utils import random_lower_string


def test_create_genre(client: TestClient) -> None:
    data = {"name": random_lower_string()}
    response = client.post("genres/", json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert "id" in content


def test_read_author(client: TestClient, db: Session) -> None:
    genre, *_ = create_random_genre(db=db)
    response = client.get(f"genres/{genre.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == genre.name
    assert content["id"] == str(genre.id)


def test_read_genres(client: TestClient, db: Session) -> None:
    create_random_genre(db=db)
    create_random_genre(db=db)
    response = client.get("authors/")
    assert response.status_code == 200
    content = response.json()
    assert content["count"] >= 2


def test_update_genre(client: TestClient, db: Session) -> None:
    genre, *_ = create_random_genre(db)
    data = {"name": random_lower_string()}
    response = client.patch(f"genres/{genre.id}", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["id"] == str(genre.id)


def test_delete_genre(client: TestClient, db: Session) -> None:
    genre, *_ = create_random_genre(db)
    response = client.delete(f"genres/{genre.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["message"] == f"Genre '{genre.name}' was successfully deleted"
