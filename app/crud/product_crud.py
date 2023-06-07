from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.schemas import ProductCreate, ProductUpdate

from app.models.product import Product
from app.models.product_type import ProductType
from app.models.category import Category

class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def get_multi_by_owner(self, db: Session, *, skip: int = 0, limit: int = 100, owner_id: int) -> List[Product]:
        return db.query(Product).join(ProductType).join(Category).filter(Category.owner_id==owner_id).offset(skip).limit(limit).all()
    
    def get_by_owner(self, db: Session, *, id: int, owner_id: int) -> Product:
        return db.query(Product).join(ProductType).join(Category).filter(Category.owner_id==owner_id).filter(Product.id==id).first()


product = CRUDProduct(Product)
