import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class InventoryMovementCreate(BaseModel):
    book_id: uuid.UUID
    change: int
    movement_date: datetime


class InventoryMovementUpdate(BaseModel):
    book_id: Optional[uuid.UUID] = None
    change: Optional[int] = None
    movement_date: Optional[datetime] = None


class InventoryMovementRead(InventoryMovementCreate):
    class Config:
        from_attributes = True


class InventoryMovementDelete(BaseModel):
    id: uuid.UUID


class InventoryMovementsPublic(BaseModel):
    data: list[InventoryMovementRead]
    count: int
