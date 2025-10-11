from fastapi import APIRouter, HTTPException

from bookstore.db.crud.book.genre import (
    create_genre,
    delete_genre,
    get_count_genres,
    get_genre,
    get_genres,
    update_genre,
)
from bookstore.db.deps import SessionDep
from bookstore.db.schemas.book.genre import (
    GenreCreate,
    GenreDelete,
    GenreRead,
    GenresPublic,
    GenreUpdate,
)

router = APIRouter(prefix="/genres", tags=["genres"])


@router.get("/", response_model=GenresPublic)
def read_genres(skip: int = 0, limit: int = 100, session: SessionDep = SessionDep):
    """Get genres."""
    genres = get_genres(session=session, skip=skip, limit=limit)
    count = get_count_genres(session=session)
    return GenresPublic(data=genres, count=count)


@router.get("/{genre_id}", response_model=GenreRead)
def read_genre(genre_id: str, session: SessionDep = SessionDep):
    """Get an genre by ID."""
    genre = get_genre(session=session, genre_id=genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre


@router.post("/", response_model=GenreRead)
def add_genre(genre_in: GenreCreate, session: SessionDep = SessionDep):
    """
    Create a new genre and return it.
    """
    genre = create_genre(session=session, genre_in=genre_in)
    return GenreRead.from_orm(genre)


@router.patch("/{genre_id}", response_model=GenreRead)
def edit_genre(session: SessionDep, genre_id: str, genre_in: GenreUpdate):
    """
    Update an genre by ID.
    """
    genre = update_genre(
        session=session,
        genre_id=genre_id,
        name=genre_in.name,
    )
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return GenreRead.from_orm(genre)


@router.delete("/{genre_id}", response_model=GenreDelete)
def remove_genre(genre_id: str, session: SessionDep = SessionDep):
    """Delete an genre by ID."""
    deleted_genre = delete_genre(session=session, genre_id=genre_id)
    if not deleted_genre:
        raise HTTPException(status_code=404, detail="Genre not found")

    return GenreDelete(
        id=deleted_genre.id,
        message=f"Genre '{deleted_genre.name}' was successfully deleted",
    )
