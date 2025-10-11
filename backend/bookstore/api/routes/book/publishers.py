from uuid import UUID

from fastapi import APIRouter, HTTPException

from bookstore.db.crud.book.publisher import (
    create_publisher,
    delete_publisher,
    get_count_publishers,
    get_publisher,
    get_publishers,
    update_publisher,
)
from bookstore.db.deps import SessionDep
from bookstore.db.schemes.book.publisher import (
    PublisherCreate,
    PublisherDelete,
    PublisherRead,
    PublishersPublic,
    PublisherUpdate,
)

router = APIRouter(prefix="/publishers", tags=["publishers"])


@router.get("/", response_model=PublishersPublic)
def read_publishers(skip: int = 0, limit: int = 100, session: SessionDep = SessionDep):
    """Get publishers."""
    publishers = get_publishers(session=session, skip=skip, limit=limit)
    count = get_count_publishers(session=session)
    return PublishersPublic(data=publishers, count=count)


@router.get("/{publisher_id}", response_model=PublisherRead)
def read_publisher(publisher_id: UUID, session: SessionDep = SessionDep):
    """Get a publisher by ID."""
    publisher = get_publisher(session=session, publisher_id=publisher_id)
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher


@router.post("/", response_model=PublisherRead)
def add_publisher(publisher_in: PublisherCreate, session: SessionDep = SessionDep):
    """
    Create a new publisher and return it.
    """
    publisher = create_publisher(session=session, publisher_in=publisher_in)
    return PublisherRead.from_orm(publisher)


@router.patch("/{publisher_id}", response_model=PublisherRead)
def edit_publisher(
    session: SessionDep, publisher_id: UUID, publisher_in: PublisherUpdate
):
    """
    Update a publisher by ID.
    """
    publisher = update_publisher(
        session=session, publisher_id=publisher_id, publisher_in=publisher_in
    )

    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return PublisherRead.from_orm(publisher)


@router.delete("/{publisher_id}", response_model=PublisherDelete)
def remove_publisher(publisher_id: UUID, session: SessionDep = SessionDep):
    """Delete a publisher by ID."""
    deleted_publisher = delete_publisher(session=session, publisher_id=publisher_id)
    if not deleted_publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")

    return PublisherDelete(
        id=deleted_publisher.id,
        message=f"Publisher '{deleted_publisher.name}' was successfully deleted",
    )
