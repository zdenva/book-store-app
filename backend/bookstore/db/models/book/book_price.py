import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class BookPrice(SQLModel, table=True):
    __tablename__ = "book_price"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    book_id: uuid.UUID = Field(foreign_key="book.id")
    price: int
    valid_from: datetime
    valid_to: Optional[datetime] = Field(default=None)
    currency_id: uuid.UUID = Field(foreign_key="currency.id")

    currency: Optional["Currency"] = Relationship(back_populates="book_prices")
    book: Optional["Book"] = Relationship(back_populates="book_prices")
