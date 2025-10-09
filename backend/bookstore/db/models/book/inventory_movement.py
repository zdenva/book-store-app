import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class InventoryMovement(SQLModel, table=True):
    __tablename__ = "inventory_movement"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    book_id: uuid.UUID = Field(foreign_key="book.id")
    change: int
    movement_date: datetime = Field(default_factory=datetime.utcnow)

    book: Optional["Book"] = Relationship(back_populates="inventory_movements")
