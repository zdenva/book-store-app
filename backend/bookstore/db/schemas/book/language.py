import uuid
from typing import Optional

from pydantic import BaseModel


class LanguageCreate(BaseModel):
    name: str
    code: str


class LanguageUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None


class LanguageRead(BaseModel):
    id: uuid.UUID
    name: str
    code: str

    class Config:
        from_attributes = True


class LanguageDelete(BaseModel):
    id: uuid.UUID
    message: str
