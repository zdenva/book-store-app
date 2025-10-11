from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.utils import (
    get_count,
    instance_create,
    instance_delete,
    instance_update,
)
from bookstore.db.models.book.genre import Genre
from bookstore.db.schemes.book.genre import GenreCreate, GenreUpdate


def get_genres(session: Session, skip: int = 0, limit: int = 100) -> list[Genre]:
    """Get genres."""
    statement = select(Genre).offset(skip).limit(limit)
    genres = session.exec(statement).all()
    return genres


def get_genre(session: Session, genre_id: UUID) -> Genre | None:
    """Get a genre by ID."""
    genre = session.get(Genre, genre_id)
    return genre


def create_genre(session: Session, genre_in: GenreCreate) -> Genre:
    """Create a new genre."""
    genre_created = instance_create(session=session, model=Genre, schema_in=genre_in)
    return genre_created


def update_genre(
    session: Session, genre_id: UUID, genre_in: GenreUpdate
) -> Genre | None:
    """Update a genre by ID."""
    genre = get_genre(session=session, genre_id=genre_id)
    genre_updated = instance_update(session=session, instance=genre, schema_in=genre_in)
    return genre_updated


def delete_genre(session: Session, genre_id: UUID) -> Genre | None:
    """Delete a genre by ID."""
    genre = get_genre(session=session, genre_id=genre_id)
    genre_deleted = instance_delete(session=session, instance=genre)
    return genre_deleted


def get_count_genres(session: Session) -> int:
    """Get total count of genre rows in table."""
    count = get_count(session=session, model=Genre)
    return count
