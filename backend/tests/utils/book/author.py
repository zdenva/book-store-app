from sqlmodel import Session

from bookstore.db.crud.book.author import create_author
from bookstore.db.models.book import Author
from bookstore.db.schemas.book.author import AuthorCreate
from tests.utils.utils import random_lower_string


def create_random_author(db: Session) -> Author:
    first_name = random_lower_string()
    last_name = random_lower_string()
    author_in = AuthorCreate(first_name=first_name, last_name=last_name)
    author = create_author(session=db, author_in=author_in)
    return author, first_name, last_name
