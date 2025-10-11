from sqlmodel import Session

from bookstore.db.crud.book.language import create_language
from bookstore.db.schemes.book.language import LanguageCreate
from tests.utils.utils import random_lower_string


def create_random_language(db: Session):
    name = random_lower_string()
    code = random_lower_string(leng=2)
    language_in = LanguageCreate(name=name, code=code)
    language = create_language(session=db, language_in=language_in)
    return language, name, code
