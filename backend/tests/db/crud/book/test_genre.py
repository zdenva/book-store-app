from fastapi.encoders import jsonable_encoder
from sqlmodel import Session

from bookstore.db.crud.book.genre import (
    delete_genre,
    get_genre,
    get_genres,
    update_genre,
)
from tests.utils.book.genre import create_random_genre
from tests.utils.utils import random_lower_string


def test_create_genre(db: Session) -> None:
    genre, name = create_random_genre(db)
    assert genre.name == name


def test_get_genre(db: Session) -> None:
    genre, name = create_random_genre(db)
    genre_2 = get_genre(session=db, genre_id=genre.id)
    assert genre_2
    assert genre.name == genre_2.name
    assert jsonable_encoder(genre) == jsonable_encoder(genre_2)


def test_update_genre(db: Session) -> None:
    genre, _ = create_random_genre(db)
    new_name = random_lower_string()
    if genre.id is not None:
        genre_2 = update_genre(
            session=db,
            genre_id=genre.id,
            name=new_name,
        )
    assert genre_2
    assert new_name == genre_2.name


def test_delete_genre(db: Session) -> None:
    genre, _ = create_random_genre(db)
    delete_genre(session=db, genre_id=genre.id)
    deleted_genre = get_genre(session=db, genre_id=genre.id)
    assert deleted_genre is None


def test_get_genres(db: Session) -> None:
    genre_1, name_1 = create_random_genre(db)
    genre_2, name_2 = create_random_genre(db)

    genres = get_genres(session=db)

    genre_ids = [a.id for a in genres]
    assert genre_1.id in genre_ids
    assert genre_2.id in genre_ids

    genre_f1 = next(a for a in genres if a.id == genre_1.id)
    assert name_1 == genre_f1.name
