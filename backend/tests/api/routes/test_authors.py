from fastapi.testclient import TestClient
from sqlmodel import Session

from tests.api.routes.utils import te_read_instances
from tests.utils.book.author import create_random_author


def test_create_author(client: TestClient) -> None:
    data = {"first_name": "Dave", "last_name": "Brown"}
    response = client.post("authors/", json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["first_name"] == data["first_name"]
    assert content["last_name"] == data["last_name"]
    assert "id" in content


def test_read_author(client: TestClient, db: Session) -> None:
    author, _ = create_random_author(db=db)
    response = client.get(f"authors/{author.id}")

    assert response.status_code == 200
    content = response.json()
    assert content["first_name"] == author.first_name
    assert content["last_name"] == author.last_name
    assert content["id"] == str(author.id)


def test_read_authors(client: TestClient, db: Session) -> None:
    te_read_instances(
        db=db,
        client=client,
        route_path="authors/",
        creation_instance=create_random_author,
    )


def test_update_author(client: TestClient, db: Session) -> None:
    author, _ = create_random_author(db)
    data = {"first_name": "Crag", "last_name": "Jones"}
    response = client.patch(f"authors/{author.id}", json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["first_name"] == data["first_name"]
    assert content["last_name"] == data["last_name"]
    assert content["id"] == str(author.id)


def test_delete_author(client: TestClient, db: Session) -> None:
    author, _ = create_random_author(db)

    response = client.delete(f"authors/{author.id}")
    assert response.status_code == 200
    content = response.json()
    assert (
        content["message"]
        == f"Author '{author.first_name} {author.last_name}' was successfully deleted"
    )
