import uuid

from sqlmodel import Field, Relationship, SQLModel

from bookstore.db.models.book.book_author import BookAuthor


class Author(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str = Field(max_length=255)
    last_name: str = Field(max_length=255)

    books: list["Book"] = Relationship(back_populates="authors", link_model=BookAuthor)
