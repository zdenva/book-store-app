import uuid
from typing import Optional

from pydantic import BaseModel


class GenreCreate(BaseModel):
    name: str


class GenreUpdate(BaseModel):
    name: Optional[str] = None


class GenreRead(BaseModel):
    id: uuid.UUID
    name: str

    class Config:
        from_attributes = True


class GenreDelete(BaseModel):
    id: uuid.UUID
    message: str
