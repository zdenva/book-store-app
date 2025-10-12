from sqlmodel import Session, select

from bookstore.db.crud.utils import instance_create, instance_delete
from bookstore.db.models.book.book_author import BookAuthor
from bookstore.db.schemas.book.book_author import BookAuthorCreate, BookAuthorDelete


def create_book_author(session: Session, book_author_in: BookAuthorCreate):
    book_author_created = instance_create(
        session=session, model=BookAuthor, schema_in=book_author_in
    )
    return book_author_created


def delete_book_author(session: Session, book_author_in: BookAuthorDelete):
    statement = select(BookAuthor).filter_by(
        book_id=book_author_in.book_id, author_id=book_author_in.author_id
    )
    book_author = session.exec(statement).first()
    book_author_deleted = instance_delete(session=session, instance=book_author)
    return book_author_deleted
