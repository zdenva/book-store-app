import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from bookstore.db.models.book.book_author import BookAuthor
from bookstore.db.models.book.book_genre import BookGenre


class Book(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=255)
    isbn: Optional[str] = Field(default=None, unique=True, index=True, max_length=13)
    num_pages: Optional[int] = Field(default=None)
    language_id: uuid.UUID = Field(foreign_key="language.id")
    publication_date: datetime = Field(default=None)
    publisher_id: uuid.UUID = Field(foreign_key="publisher.id")

    genres: list["Genre"] = Relationship(back_populates="books", link_model=BookGenre)
    authors: list["Author"] = Relationship(
        back_populates="books", link_model=BookAuthor
    )

    language: Optional["Language"] = Relationship(back_populates="books")
    publisher: Optional["Publisher"] = Relationship(back_populates="books")
    inventory_movements: list["InventoryMovement"] = Relationship(back_populates="book")
    inventory: "Inventory" = Relationship(back_populates="book")
