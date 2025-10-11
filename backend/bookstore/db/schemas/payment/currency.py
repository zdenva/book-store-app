import uuid
from typing import List, Optional

from pydantic import BaseModel, Field


class CurrencyCreate(BaseModel):
    code: str = Field(max_length=3)
    symbol: str = Field(max_length=5)
    name: str
    minor_unit: Optional[int] = Field(default=2)


class CurrencyUpdate(BaseModel):
    code: Optional[str] = Field(default=None, max_length=3)
    symbol: Optional[str] = Field(default=None, max_length=5)
    name: Optional[str] = None
    minor_unit: Optional[int] = None


class CurrencyRead(CurrencyCreate):
    id: uuid.UUID

    class Config:
        from_attributes = True


class CurrencyDelete(BaseModel):
    id: uuid.UUID
    message: str


class CurrenciesPublic(BaseModel):
    data: List[CurrencyRead]
    count: int
