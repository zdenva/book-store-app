from uuid import UUID

from fastapi import APIRouter, HTTPException, Query

from bookstore.db.crud.book.book_genre import create_book_genre, delete_book_genre
from bookstore.db.deps import SessionDep
from bookstore.db.schemas.book.book_genre import (
    BookGenreCreate,
    BookGenreDelete,
    BookGenreRead,
)

router = APIRouter(prefix="/book-genre", tags=["book-genre"])


@router.post("/", response_model=BookGenreRead)
def add_book_genre(book_genre_in: BookGenreCreate, session: SessionDep = SessionDep):
    """
    Create a new book genre and return it.
    """
    book_genre = create_book_genre(session=session, book_genre_in=book_genre_in)
    return BookGenreRead.from_orm(book_genre)


@router.delete("/", response_model=BookGenreDelete)
def remove_book_genre(
    book_id: UUID,
    genre_id: UUID,
    session: SessionDep = SessionDep,
):
    """Delete a book genre by ID."""
    book_genre_in = BookGenreDelete(book_id=book_id, genre_id=genre_id)
    deleted_book_genre = delete_book_genre(session=session, book_genre_in=book_genre_in)

    if not deleted_book_genre:
        raise HTTPException(status_code=404, detail="Book genre not found")

    return BookGenreDelete(
        id=deleted_book_genre.id,
        message="Book genre row was successfully deleted",
    )
