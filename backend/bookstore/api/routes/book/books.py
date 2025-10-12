from uuid import UUID

from fastapi import APIRouter, HTTPException

from bookstore.db.crud.book.book import (
    create_book,
    delete_book,
    get_book,
    get_books,
    get_count_books,
    update_book,
)
from bookstore.db.crud.book.inventory import create_inventory
from bookstore.db.schemas.book.inventory import InventoryCreate

from bookstore.db.deps import SessionDep
from bookstore.db.schemas.book.book import (
    BookCreate,
    BookDelete,
    BookRead,
    BooksPublic,
    BookUpdate,
)

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=BooksPublic)
def read_books(skip: int = 0, limit: int = 100, session: SessionDep = SessionDep):
    """Get books."""
    books = get_books(session=session, skip=skip, limit=limit)
    count = get_count_books(session=session)
    return BooksPublic(data=books, count=count)


@router.get("/{book_id}", response_model=BookRead)
def read_book(book_id: UUID, session: SessionDep = SessionDep):
    """Get a book by ID."""
    book = get_book(session=session, book_id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", response_model=BookRead)
def add_book(book_in: BookCreate, session: SessionDep = SessionDep):
    """
    Create a new book and return it.
    """
    book = create_book(session=session, book_in=book_in)
    if book is not None:
        inventory = InventoryCreate(book_id=book.id, quantity=0)
        create_inventory(session=session, inventory_in=inventory)
    return BookRead.from_orm(book)


@router.patch("/{book_id}", response_model=BookRead)
def edit_book(session: SessionDep, book_id: UUID, book_in: BookUpdate):
    """
    Update a book by ID.
    """
    book = update_book(session=session, book_id=book_id, book_in=book_in)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return BookRead.from_orm(book)


@router.delete("/{book_id}", response_model=BookDelete)
def remove_book(book_id: UUID, session: SessionDep = SessionDep):
    """Delete a book by ID."""
    deleted_book = delete_book(session=session, book_id=book_id)
    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return BookDelete(
        id=deleted_book.id,
        message=f"Book '{deleted_book.name}' was successfully deleted",
    )
