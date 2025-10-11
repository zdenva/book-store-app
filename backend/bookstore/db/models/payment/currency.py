import uuid

from sqlmodel import Field, Relationship, SQLModel


class Currency(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    code: str = Field(max_length=3)
    symbol: str = Field(max_length=5)
    name: str
    minor_unit: int = Field(default=2)

    book_prices: list["BookPrice"] = Relationship(back_populates="currency")
