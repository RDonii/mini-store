from typing import Optional
from datetime import datetime
from pydantic import BaseModel, condecimal

from app.models.product import CurrencyEnum


class ProductBase(BaseModel):
    model: Optional[str] = None
    unit_cost: condecimal(max_digits=7, decimal_places=2)
    unit_price: condecimal(max_digits=7, decimal_places=2)
    currency: CurrencyEnum
    amount: Optional[int] = 0
    type_id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(ProductBase):
    id: Optional[int] = None
    created: datetime
    updated: Optional[datetime] = None

    class Config:
        orm_mode = True


class Product(ProductInDBBase):
    pass


class ProductInDB(ProductInDBBase):
    pass
