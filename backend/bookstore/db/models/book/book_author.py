import uuid

from sqlmodel import Field, SQLModel


class BookAuthor(SQLModel, table=True):
    __tablename__ = "book_author"
    book_id: uuid.UUID = Field(foreign_key="book.id", primary_key=True)
    author_id: uuid.UUID = Field(foreign_key="author.id", primary_key=True)
