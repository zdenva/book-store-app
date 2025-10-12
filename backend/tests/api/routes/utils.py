from fastapi.testclient import TestClient
from sqlmodel import Session


def te_read_instances(
    db: Session, client: TestClient, route_path: str, creation_instance
):
    response_before = client.get(route_path)
    assert response_before.status_code == 200
    count_before = response_before.json()["count"]

    creation_instance(db=db)

    response_after = client.get(route_path)
    assert response_after.status_code == 200
    counter_after = response_after.json()["count"]
    assert counter_after == count_before + 1
