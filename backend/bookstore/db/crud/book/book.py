from uuid import UUID

from sqlalchemy.orm import joinedload
from sqlmodel import Session, select

from bookstore.db.crud.utils import (
    get_count,
    instance_create,
    instance_delete,
    instance_update,
)
from bookstore.db.models.book.book import Book
from bookstore.db.schemas.book.book import BookCreate, BookUpdate


def get_books(session: Session, skip: int = 0, limit: int = 100) -> list[Book]:
    """Get books."""
    statement = select(Book).offset(skip).limit(limit)
    books = session.exec(statement).all()
    return books


def get_book(session: Session, book_id: UUID) -> Book | None:
    """Get a book by ID."""
    book = (
        session.query(Book)
        .options(
            joinedload(Book.genres),
            joinedload(Book.authors),
            joinedload(Book.language),
            joinedload(Book.publisher),
        )
        .filter(Book.id == book_id)
        .first()
    )
    return book


def create_book(session: Session, book_in: BookCreate) -> Book:
    """Create a new book."""
    book_created = instance_create(session=session, model=Book, schema_in=book_in)
    return book_created


def update_book(session: Session, book_id: UUID, book_in: BookUpdate) -> Book | None:
    """Update a book by ID."""
    book = get_book(session=session, book_id=book_id)
    book_updated = instance_update(session=session, instance=book, schema_in=book_in)
    return book_updated


def delete_book(session: Session, book_id: UUID) -> Book | None:
    """Delete a book by ID."""
    book = get_book(session=session, book_id=book_id)
    book_deleted = instance_delete(session=session, instance=book)
    return book_deleted


def get_count_books(session: Session) -> int:
    """Get total count of book rows in table."""
    count = get_count(session=session, model=Book)
    return count
