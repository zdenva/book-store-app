from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.utils import (
    get_count,
    instance_create,
    instance_delete,
    instance_update,
)
from bookstore.db.models.book.publisher import Publisher
from bookstore.db.schemas.book.publisher import PublisherCreate, PublisherUpdate


def get_publishers(
    session: Session, skip: int = 0, limit: int = 100
) -> list[Publisher]:
    """Get publishers."""
    statement = select(Publisher).offset(skip).limit(limit)
    publisher = session.exec(statement).all()
    return publisher


def get_publisher(session: Session, publisher_id: UUID) -> Publisher | None:
    """Get a publisher by ID."""
    publisher = session.get(Publisher, publisher_id)
    if not publisher:
        return None
    return publisher


def create_publisher(session: Session, publisher_in: PublisherCreate) -> Publisher:
    """Create a new publisher."""
    publisher_created = instance_create(
        session=session, model=Publisher, schema_in=publisher_in
    )
    return publisher_created


def update_publisher(
    session: Session, publisher_id: UUID, publisher_in: PublisherUpdate
) -> Publisher | None:
    """Update a publisher by ID."""
    publisher = get_publisher(session=session, publisher_id=publisher_id)
    publisher_updated = instance_update(
        session=session, instance=publisher, schema_in=publisher_in
    )
    return publisher_updated


def delete_publisher(session: Session, publisher_id: UUID) -> Publisher:
    """Delete a publisher by ID."""
    publisher = get_publisher(session=session, publisher_id=publisher_id)
    publisher_deleted = instance_delete(session=session, instance=publisher)
    return publisher_deleted


def get_count_publishers(session: Session) -> int:
    """Get total count of publisher rows in table."""
    count = get_count(session=session, model=Publisher)
    return count
