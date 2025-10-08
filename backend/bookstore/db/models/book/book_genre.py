import uuid

from sqlmodel import Field, SQLModel


class BookGenre(SQLModel, table=True):
    __tablename__ = "book_genre"
    book_id: uuid.UUID = Field(foreign_key="book.id", primary_key=True)
    genre: uuid.UUID = Field(foreign_key="genre.id", primary_key=True)
