from sqlmodel import Session, select

from bookstore.db.crud.utils import instance_create, instance_delete
from bookstore.db.models.book.book_genre import BookGenre
from bookstore.db.schemas.book.book_genre import BookGenreCreate, BookGenreDelete


def create_book_genre(session: Session, book_genre_in: BookGenreCreate):
    book_genre_created = instance_create(
        session=session, model=BookGenre, schema_in=book_genre_in
    )
    return book_genre_created


def delete_book_genre(session: Session, book_genre_in: BookGenreDelete):
    statement = select(BookGenre).filter_by(
        book_id=book_genre_in.book_id, genre_id=book_genre_in.genre_id
    )
    book_genre = session.exec(statement).first()
    book_genre_deleted = instance_delete(session=session, instance=book_genre)
    return book_genre_deleted
