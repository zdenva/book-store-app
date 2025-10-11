from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.utils import (
    get_count,
    instance_create,
    instance_delete,
    instance_update,
)
from bookstore.db.models.book.book_price import BookPrice
from bookstore.db.schemas.book.book_price import BookPriceCreate, BookPriceUpdate


def get_book_prices(
    session: Session, skip: int = 0, limit: int = 100
) -> list[BookPrice]:
    """Get book prices."""
    statement = select(BookPrice).offset(skip).limit(limit)
    book_prices = session.exec(statement).all()
    return book_prices


def get_book_price(session: Session, book_price_id: UUID) -> BookPrice | None:
    """Get a book price by ID."""
    book_price = session.get(BookPrice, book_price_id)
    return book_price


def create_book_price(session: Session, book_price_in: BookPriceCreate) -> BookPrice:
    """Create a new book price."""
    book_price_created = instance_create(
        session=session, model=BookPrice, schema_in=book_price_in
    )
    return book_price_created


def update_book_price(
    session: Session, book_price_id: UUID, book_price_in: BookPriceUpdate
) -> BookPrice | None:
    """Update a book price by ID."""
    book_price = get_book_price(session=session, book_price_id=book_price_id)
    book_price_updated = instance_update(
        session=session, instance=book_price, schema_in=book_price_in
    )
    return book_price_updated


def delete_book_price(session: Session, book_price_id: UUID) -> BookPrice:
    """Delete a book price by ID."""
    book_price = get_book_price(session=session, book_price_id=book_price_id)
    book_price_deleted = instance_delete(session=session, instance=book_price)
    return book_price_deleted


def get_count_book_prices(session: Session) -> int:
    """Get total count of book price rows in table."""
    count = get_count(session=session, model=BookPrice)
    return count
