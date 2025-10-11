import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BookPriceCreate(BaseModel):
    book_id: uuid.UUID
    price: int
    valid_from: datetime
    valid_to: Optional[datetime] = None
    currency_id: uuid.UUID


class BookPriceUpdate(BaseModel):
    book_id: Optional[uuid.UUID] = None
    price: Optional[int] = None
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None
    currency_id: Optional[uuid.UUID] = None


class BookPriceRead(BookPriceCreate):
    id: uuid.UUID

    class Config:
        from_attributes = True


class BookPriceDelete(BaseModel):
    id: uuid.UUID
    message: str


class BookPricesPublic(BaseModel):
    data: list[BookPriceRead]
    count: int
