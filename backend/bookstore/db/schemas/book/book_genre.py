import uuid

from pydantic import BaseModel


class BookGenreBase(BaseModel):
    book_id: uuid.UUID
    genre_id: uuid.UUID


class BookGenreRead(BookGenreBase):
    pass

    class Config:
        from_attributes = True


class BookGenreCreate(BookGenreBase):
    pass


class BookGenreDelete(BookGenreBase):
    pass
