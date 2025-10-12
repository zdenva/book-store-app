from fastapi.encoders import jsonable_encoder
from sqlmodel import Session

from bookstore.db.crud.book.language import (
    delete_language,
    get_language,
    get_languages,
    update_language,
)
from bookstore.db.schemas.book.language import LanguageUpdate
from tests.utils.book.language import create_random_language
from tests.utils.utils import random_lower_string


def test_create_language(db: Session) -> None:
    language, language_in = create_random_language(db)
    assert language.name == language_in.name
    assert language.code == language_in.code


def test_get_language(db: Session) -> None:
    language, _ = create_random_language(db)
    language_2 = get_language(session=db, language_id=language.id)
    assert jsonable_encoder(language) == jsonable_encoder(language_2)


def test_update_language(db: Session) -> None:
    language, _ = create_random_language(db)
    new_name = random_lower_string()
    new_code = random_lower_string(leng=2)
    language_in = LanguageUpdate(name=new_name, code=new_code)
    if language.id is not None:
        language_2 = update_language(
            session=db, language_id=language.id, language_in=language_in
        )
    assert language_2
    assert new_name == language_2.name
    assert new_code == language_2.code


def test_delete_language(db: Session) -> None:
    language, _ = create_random_language(db)
    delete_language(session=db, language_id=language.id)
    deleted_language = get_language(session=db, language_id=language.id)
    assert deleted_language is None


def test_get_languages(db: Session) -> None:
    language_1, language_in_1 = create_random_language(db)
    language_2, language_in_2 = create_random_language(db)

    languages = get_languages(session=db, limit=9999)

    language_ids = [a.id for a in languages]
    assert language_1.id in language_ids
    assert language_2.id in language_ids

    language_f1 = next(a for a in languages if a.id == language_1.id)
    assert language_in_1.name == language_f1.name
    assert language_in_1.code == language_f1.code
