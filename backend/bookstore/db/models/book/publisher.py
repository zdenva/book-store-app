import uuid
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Publisher(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(unique=True, index=True, max_length=255)

    book: Optional["Book"] = Relationship(back_populates="publisher")  # noqa: F821
