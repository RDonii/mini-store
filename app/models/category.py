from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship


from app.db.base_class import Base

class Category(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(25), nullable=False, index=True)
    description = Column(String(255))
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="categories")
    product_types = relationship("ProductType", back_populates="category")
    

    __table_args__ = (
        UniqueConstraint('owner_id', 'title', name='owner_title'),
    )
