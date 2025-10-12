import uuid
from typing import Optional

from pydantic import BaseModel


class InventoryCreate(BaseModel):
    book_id: uuid.UUID
    quantity: int


class InventoryUpdate(BaseModel):
    quantity: Optional[int] = 0


class InventoryRead(BaseModel):
    book_id: uuid.UUID
    quantity: int

    class Config:
        from_attributes = True


class InventoriesPublic(BaseModel):
    data: list[InventoryRead]
    count: int
