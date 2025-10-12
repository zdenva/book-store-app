from fastapi.encoders import jsonable_encoder
from sqlmodel import Session

from bookstore.db.crud.book.author import (
    delete_author,
    get_author,
    get_authors,
    update_author,
)
from bookstore.db.schemas.book.author import AuthorUpdate
from tests.utils.book.author import create_random_author
from tests.utils.utils import random_lower_string


def test_create_author(db: Session) -> None:
    author, author_in = create_random_author(db)
    assert author.first_name == author_in.first_name
    assert author.last_name == author_in.last_name


def test_get_author(db: Session) -> None:
    author, _ = create_random_author(db)
    author_2 = get_author(session=db, author_id=author.id)
    assert jsonable_encoder(author) == jsonable_encoder(author_2)


def test_update_author(db: Session) -> None:
    author, *_ = create_random_author(db)
    new_first_name = random_lower_string()
    new_last_name = random_lower_string()
    author_in = AuthorUpdate(first_name=new_first_name, last_name=new_last_name)
    if author.id is not None:
        author2 = update_author(session=db, author_id=author.id, author_in=author_in)
    assert author2
    assert author_in.first_name == author2.first_name
    assert author_in.last_name == author2.last_name


def test_delete_author(db: Session) -> None:
    author, *_ = create_random_author(db)
    delete_author(session=db, author_id=author.id)
    deleted_author = get_author(session=db, author_id=author.id)
    assert deleted_author is None


def test_get_authors(db: Session) -> None:
    author1, author_in_1 = create_random_author(db)
    author2, author_in_2 = create_random_author(db)

    authors = get_authors(session=db, limit=9999)

    author_ids = [a.id for a in authors]
    assert author1.id in author_ids
    assert author2.id in author_ids

    author_f1 = next(a for a in authors if a.id == author1.id)
    assert author_in_1.first_name == author_f1.first_name
    assert author_in_1.last_name == author_f1.last_name
