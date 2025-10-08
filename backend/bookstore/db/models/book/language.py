import uuid
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Language(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(max_length=255)
    code: str = Field(max_length=2)

    book: Optional["Book"] = Relationship(back_populates="language")
