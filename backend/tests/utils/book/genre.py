from sqlmodel import Session

from bookstore.db.crud.book.genre import create_genre
from bookstore.db.schemas.book.genre import GenreCreate
from tests.utils.utils import random_lower_string


def create_random_genre(db: Session):
    name = random_lower_string()
    genre_in = GenreCreate(name=name)
    genre = create_genre(session=db, genre_in=genre_in)
    return genre, name
