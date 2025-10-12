import uuid
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Inventory(SQLModel, table=True):
    book_id: uuid.UUID = Field(foreign_key="book.id", primary_key=True)
    quantity: int

    book: "Book" = Relationship(back_populates="inventory")
