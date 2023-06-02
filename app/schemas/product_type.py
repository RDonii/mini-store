from typing import Optional
from pydantic import BaseModel

from app.models.product_type import MeasureEnum


class ProductTypeBase(BaseModel):
    title: str
    measure: Optional[MeasureEnum]
    category_id: int


class ProductTypeCreate(ProductTypeBase):
    pass


class ProductTypeUpdate(ProductTypeBase):
    pass


class ProductTypeInDBBase(ProductTypeBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class ProductType(ProductTypeInDBBase):
    pass


class ProductTypeInDB(ProductTypeInDBBase):
    pass
