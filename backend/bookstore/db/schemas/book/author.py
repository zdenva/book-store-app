import uuid
from typing import Optional

from pydantic import BaseModel


class AuthorCreate(BaseModel):
    first_name: str
    last_name: str


class AuthorUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class AuthorRead(BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str

    class Config:
        from_attributes = True


class AuthorDelete(BaseModel):
    id: uuid.UUID
    message: str
