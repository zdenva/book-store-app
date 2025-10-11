from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.utils import get_count
from bookstore.db.models.book.publisher import Publisher
from bookstore.db.schemes.book.publisher import PublisherCreate


def get_publishers(
    session: Session, skip: int = 0, limit: int = 100
) -> list[Publisher]:
    """Get publishers."""
    statement = select(Publisher).offset(skip).limit(limit)
    return session.exec(statement).all()


def get_publisher(session: Session, publisher_id: UUID) -> Publisher | None:
    """Get an publisher by ID."""
    publisher = session.get(Publisher, publisher_id)
    if not publisher:
        return None
    return publisher


def create_publisher(session: Session, publisher_in: PublisherCreate) -> Publisher:
    """Create a new publisher."""
    publisher = Publisher(**publisher_in.dict())

    session.add(publisher)
    session.commit()
    session.refresh(publisher)

    return publisher


def update_publisher(
    session: Session, publisher_id: str, name: str
) -> Publisher | None:
    """Update an publisher by ID."""
    publisher = get_publisher(session=session, publisher_id=publisher_id)
    if not publisher:
        return None
    publisher.name = name
    session.add(publisher)
    session.commit()
    session.refresh(publisher)
    return publisher


def delete_publisher(session: Session, publisher_id) -> Publisher:
    """Delete an publisher by ID."""
    publisher = get_publisher(session=session, publisher_id=publisher_id)
    if not publisher:
        return None
    session.delete(publisher)
    session.commit()
    return publisher


def get_count_publishers(session: Session) -> int:
    """Get total count of publisher rows in table."""
    return get_count(session=session, model=Publisher)
