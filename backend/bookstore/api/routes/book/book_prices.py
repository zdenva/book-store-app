from uuid import UUID

from fastapi import APIRouter, HTTPException

from bookstore.db.crud.book.book_price import (
    create_book_price,
    delete_book_price,
    get_book_price,
    get_book_prices,
    get_count_book_prices,
    update_book_price,
)
from bookstore.db.deps import SessionDep
from bookstore.db.schemes.book.book_price import (
    BookPriceCreate,
    BookPriceDelete,
    BookPriceRead,
    BookPricesPublic,
    BookPriceUpdate,
)

router = APIRouter(prefix="/book_prices", tags=["book_prices"])


@router.get("/", response_model=BookPricesPublic)
def read_book_prices(skip: int = 0, limit: int = 100, session: SessionDep = SessionDep):
    """Get book prices."""
    book_prices = get_book_prices(session=session, skip=skip, limit=limit)
    count = get_count_book_prices(session=session)
    return BookPricesPublic(data=book_prices, count=count)


@router.get("/{book_price_id}", response_model=BookPriceRead)
def read_book_price(book_price_id: UUID, session: SessionDep = SessionDep):
    """Get a book price by ID."""
    book_price = get_book_price(session=session, book_price_id=book_price_id)
    if not book_price:
        raise HTTPException(status_code=404, detail="Book price not found")
    return book_price


@router.post("/", response_model=BookPriceRead)
def add_book_price(book_price_in: BookPriceCreate, session: SessionDep = SessionDep):
    """
    Create a new book price and return it.
    """
    book_price = create_book_price(session=session, book_price_in=book_price_in)
    return BookPriceRead.from_orm(book_price)


@router.patch("/{book_price_id}", response_model=BookPriceRead)
def edit_book_price(
    session: SessionDep, book_price_id: UUID, book_price_in: BookPriceUpdate
):
    """
    Update a book price by ID.
    """
    book_price = update_book_price(
        session=session,
        book_price_id=book_price_id,
        book_price_in=book_price_in,
    )
    if not book_price:
        raise HTTPException(status_code=404, detail="Book price not found")
    return BookPriceRead.from_orm(book_price)


@router.delete("/{book_price_id}", response_model=BookPriceDelete)
def remove_book_price(book_price_id: UUID, session: SessionDep = SessionDep):
    """Delete a book price by ID."""
    deleted_book_price = delete_book_price(session=session, book_price_id=book_price_id)

    if not deleted_book_price:
        raise HTTPException(status_code=404, detail="Book price not found")

    return BookPriceDelete(
        id=deleted_book_price.id,
        message="Book price row was successfully deleted",
    )
