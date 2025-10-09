from fastapi.encoders import jsonable_encoder
from sqlmodel import Session

from bookstore.db.crud.book.author import (
    get_author,
    update_author,
    delete_author,
    get_authors,
)
from tests.utils.book.author import create_random_author
from tests.utils.utils import random_lower_string


def test_create_author(db: Session) -> None:
    author, first_name, last_name = create_random_author(db)
    assert author.first_name == first_name
    assert author.last_name == last_name


def test_get_author(db: Session) -> None:
    author, first_name, last_name = create_random_author(db)
    author_2 = get_author(session=db, author_id=author.id)
    assert author_2
    assert author.first_name == author_2.first_name
    assert author.last_name == author_2.last_name
    assert jsonable_encoder(author) == jsonable_encoder(author_2)


def test_update_author(db: Session) -> None:
    author, *_ = create_random_author(db)
    new_first_name = random_lower_string()
    new_last_name = random_lower_string()
    if author.id is not None:
        author2 = update_author(
            session=db,
            author_id=author.id,
            first_name=new_first_name,
            last_name=new_last_name,
        )
    assert author2
    assert new_first_name == author2.first_name
    assert new_last_name == author2.last_name


def test_delete_author(db: Session) -> None:
    author, *_ = create_random_author(db)
    delete_author(session=db, author_id=author.id)
    deleted_author = get_author(session=db, author_id=author.id)
    assert deleted_author is None


def test_get_authors(db: Session) -> None:
    author1, first_name1, last_name1 = create_random_author(db)
    author2, first_name2, last_name2 = create_random_author(db)

    authors = get_authors(session=db)

    author_ids = [a.id for a in authors]
    assert author1.id in author_ids
    assert author2.id in author_ids

    author_f1 = next(a for a in authors if a.id == author1.id)
    assert first_name1 == author_f1.first_name
    assert last_name1 == author_f1.last_name
