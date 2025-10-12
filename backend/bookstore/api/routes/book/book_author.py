from uuid import UUID

from fastapi import APIRouter, HTTPException

from bookstore.db.crud.book.book_author import create_book_author, delete_book_author
from bookstore.db.deps import SessionDep
from bookstore.db.schemas.book.book_author import (
    BookAuthorCreate,
    BookAuthorDelete,
    BookAuthorRead,
)

router = APIRouter(prefix="/book-author", tags=["book-author"])


@router.post("/", response_model=BookAuthorRead)
def add_book_author(book_author_in: BookAuthorCreate, session: SessionDep = SessionDep):
    """
    Create a new book author and return it.
    """
    book_author = create_book_author(session=session, book_author_in=book_author_in)
    return BookAuthorRead.from_orm(book_author)


@router.delete("/", response_model=BookAuthorDelete)
def remove_book_author(
    book_id: UUID, author_id: UUID, session: SessionDep = SessionDep
):
    """Delete a book author by ID."""
    book_genre_in = BookAuthorDelete(book_id=book_id, author_id=author_id)
    deleted_book_author = delete_book_author(
        session=session, book_genre_in=book_genre_in
    )

    if not deleted_book_author:
        raise HTTPException(status_code=404, detail="Book author not found")

    return BookAuthorDelete(
        id=deleted_book_author.id,
        message="Book author row was successfully deleted",
    )
