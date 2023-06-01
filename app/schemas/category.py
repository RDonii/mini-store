from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    title: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    owner_id: int


class CategoryUpdate(CategoryBase):
    pass


class CategoryInDBBase(CategoryBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Category(CategoryInDBBase):
    owner_id: int


class CategoryInDB(CategoryInDBBase):
    owner_id: int
