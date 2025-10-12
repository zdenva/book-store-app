import uuid

from pydantic import BaseModel


class BookAuthorBase(BaseModel):
    book_id: uuid.UUID
    author_id: uuid.UUID


class BookAuthorRead(BookAuthorBase):
    pass

    class Config:
        from_attributes = True


class BookAuthorCreate(BookAuthorBase):
    pass


class BookAuthorDelete(BookAuthorBase):
    pass
