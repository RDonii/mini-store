from typing import List, Union
from sqlalchemy.orm import Session

from app.models.category import Category
from app.crud.base import CRUDBase
from app.schemas.category import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def get_multi_by_owner(self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100) -> List[Category]:
        return db.query(self.model).filter(self.model.owner_id==owner_id).offset(skip).limit(limit).all()
    
    def get_by_title_owner(self, db: Session, *, owner_id: int, title: str) -> Union[Category, None]:
        return db.query(self.model).filter(self.model.owner_id==owner_id, self.model.title==title).first()

category = CRUDCategory(Category)
