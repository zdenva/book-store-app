from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.utils import (
    get_count,
    instance_create,
    instance_delete,
    instance_update,
)
from bookstore.db.models.book.author import Author
from bookstore.db.schemas.book.author import AuthorCreate, AuthorUpdate


def get_authors(session: Session, skip: int = 0, limit: int = 100) -> list[Author]:
    """Get authors."""
    statement = select(Author).offset(skip).limit(limit)
    authors = session.exec(statement).all()
    return authors


def get_author(session: Session, author_id: UUID) -> Author | None:
    """Get an author by ID."""
    author = session.get(Author, author_id)
    return author


def create_author(session: Session, author_in: AuthorCreate) -> Author:
    """Create a new author."""
    author = instance_create(session=session, instance=Author, schema_in=author_in)
    return author


def update_author(
    session: Session, author_id: UUID, author_in: AuthorUpdate
) -> Author | None:
    """Update an author by ID."""
    author = get_author(session=session, author_id=author_id)
    author_updated = instance_update(
        session=session, instance=author, schema_in=author_in
    )
    return author_updated


def delete_author(session: Session, author_id: UUID) -> Author:
    """Delete an author by ID."""
    author = get_author(session=session, author_id=author_id)
    author_deleted = instance_delete(session=session, instance=author)
    return author_deleted


def get_count_authors(session: Session) -> int:
    """Get total count of author rows in table."""
    count = get_count(session=session, model=Author)
    return count
