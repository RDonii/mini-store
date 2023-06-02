from typing import List, Union
from sqlalchemy.orm import Session

from app.models.product_type import ProductType
from app.crud.base import CRUDBase
from app.schemas import ProductTypeCreate, ProductTypeUpdate

class CRUDProductType(CRUDBase[ProductType, ProductTypeCreate, ProductTypeUpdate]):
    def get_multi_by_category(self, db: Session, *, category_id: int, skip: int = 0, limit: int = 100) -> List[ProductType]:
        return db.query(self.model).filter(self.model.category_id==category_id).offset(skip).limit(limit).all()
    
    def get_multi_by_owner(self, db: Session, *, owner_id: int) -> List[ProductType]:
        return db.query(self.model).filter(self.model.category.has(owner_id=owner_id)).all()
    
    def get_by_title_category(self, db: Session, *, category_id: int, title: str) -> Union[ProductType, None]:
        return db.query(self.model).filter(self.model.category_id==category_id, self.model.title==title).first()


product_type = CRUDProductType(ProductType)