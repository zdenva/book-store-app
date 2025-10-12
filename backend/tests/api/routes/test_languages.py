from fastapi.testclient import TestClient
from sqlmodel import Session

from tests.api.routes.utils import te_read_instances
from tests.utils.book.language import create_random_language


def test_create_language(client: TestClient) -> None:
    data = {"name": "english", "code": "en"}

    response = client.post("languages/", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["code"] == data["code"]
    assert "id" in content


def test_read_author(client: TestClient, db: Session) -> None:
    language, _ = create_random_language(db=db)

    response = client.get(f"languages/{language.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == language.name
    assert content["code"] == language.code
    assert content["id"] == str(language.id)


def test_read_languages(client: TestClient, db: Session) -> None:
    te_read_instances(
        db=db,
        client=client,
        route_path="languages/",
        creation_instance=create_random_language,
    )


def test_update_language(client: TestClient, db: Session) -> None:
    language, _ = create_random_language(db)
    data = {"name": "czech", "code": "cz"}

    response = client.patch(f"languages/{language.id}", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["code"] == data["code"]
    assert content["id"] == str(language.id)


def test_delete_language(client: TestClient, db: Session) -> None:
    language, _ = create_random_language(db)

    response = client.delete(f"languages/{language.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["message"] == f"Language '{language.name}' was successfully deleted"
