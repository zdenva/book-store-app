from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class InventoryMovementCreate(BaseModel):
    book_id: UUID
    change: int
    note: Optional[str] = None


class InventoryMovementRead(InventoryMovementCreate):
    id: UUID
    movement_date: datetime

    class Config:
        from_attributes = True


class InventoryMovementsPublic(BaseModel):
    data: list[InventoryMovementRead]
    count: int
