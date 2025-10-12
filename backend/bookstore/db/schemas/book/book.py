import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from bookstore.db.schemas.book.author import AuthorRead
from bookstore.db.schemas.book.genre import GenreRead
from bookstore.db.schemas.book.language import LanguageRead
from bookstore.db.schemas.book.publisher import PublisherRead


class BookBase(BaseModel):
    title: str = Field(max_length=255)
    description: Optional[str] = None
    isbn: Optional[str] = Field(max_length=13)
    num_pages: Optional[int] = None
    language_id: uuid.UUID
    publication_date: Optional[datetime] = None
    publisher_id: uuid.UUID


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=255)
    description: Optional[str] = None
    isbn: Optional[str] = Field(default=None, max_length=13)
    num_pages: Optional[int] = None
    language_id: Optional[uuid.UUID] = None
    publication_date: Optional[datetime] = None
    publisher_id: Optional[uuid.UUID] = None


class BookRead(BaseModel):
    id: uuid.UUID
    title: str = Field(max_length=255)
    description: Optional[str]
    isbn: Optional[str] = Field(max_length=13)
    num_pages: Optional[int] = None
    language: LanguageRead
    publication_date: Optional[datetime] = None
    publisher: PublisherRead
    genres: list[GenreRead]
    authors: list[AuthorRead]

    class Config:
        from_attributes = True


class BookDelete(BaseModel):
    id: uuid.UUID
    message: str


class BooksPublic(BaseModel):
    data: list[BookRead]
    count: int
