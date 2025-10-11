import uuid
from typing import Optional

from pydantic import BaseModel


class PublisherCreate(BaseModel):
    name: str


class PublisherUpdate(BaseModel):
    name: Optional[str] = None


class PublisherRead(BaseModel):
    id: uuid.UUID
    name: str

    class Config:
        from_attributes = True


class PublisherDelete(BaseModel):
    id: uuid.UUID
    message: str


class PublishersPublic(BaseModel):
    data: list[PublisherRead]
    count: int
