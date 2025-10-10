from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.utils import get_count
from bookstore.db.models.book.genre import Genre
from bookstore.db.schemas.book.genre import GenreCreate


def get_genres(session: Session, skip: int = 0, limit: int = 100) -> list[Genre]:
    """Get genres."""
    statement = select(Genre).offset(skip).limit(limit)
    return session.exec(statement).all()


def get_genre(session: Session, genre_id: UUID) -> Genre | None:
    """Get an genre by ID."""
    genre = session.get(Genre, genre_id)
    if not genre:
        return None
    return genre


def create_genre(session: Session, genre_in: GenreCreate) -> Genre:
    """Create a new genre."""
    genre = Genre(**genre_in.dict())

    session.add(genre)
    session.commit()
    session.refresh(genre)

    return genre


def update_genre(session: Session, genre_id: str, name: str) -> Genre | None:
    """Update an genre by ID."""
    genre = get_genre(session=session, genre_id=genre_id)
    if not genre:
        return None
    genre.name = name
    session.add(genre)
    session.commit()
    session.refresh(genre)
    return genre


def delete_genre(session: Session, genre_id) -> Genre:
    """Delete an genre by ID."""
    genre = get_genre(session=session, genre_id=genre_id)
    if not genre:
        return None
    session.delete(genre)
    session.commit()
    return genre


def get_count_genres(session: Session) -> int:
    """Get total count of genre rows in table."""
    return get_count(session=session, model=Genre)
