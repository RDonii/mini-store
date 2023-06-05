from typing import Optional
from pydantic import BaseModel

from app.models.product_type import MeasureEnum


class ProductTypeBase(BaseModel):
    title: str
    measure: Optional[MeasureEnum]


class ProductTypeCreate(ProductTypeBase):
    category_id: int


class ProductTypeUpdate(ProductTypeBase):
    pass


class ProductTypeInDBBase(ProductTypeBase):
    id: Optional[int] = None
    category_id: int

    class Config:
        orm_mode = True


class ProductType(ProductTypeInDBBase):
    pass


class ProductTypeInDB(ProductTypeInDBBase):
    pass
