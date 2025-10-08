import uuid

from sqlmodel import Field, Relationship, SQLModel

from bookstore.db.models.book.book_genre import BookGenre


class Genre(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(unique=True, index=True)

    books: list["Book"] = Relationship(back_populates="genres", link_model=BookGenre)
