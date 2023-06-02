import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class MeasureEnum(enum.Enum):
    piece = 1
    pack = 2
    kg = 3
    meter = 4


class ProductType(Base):
    __tablename__ = 'product_type'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(25), nullable=False)
    measure = Column(Enum(MeasureEnum))
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    category = relationship('Category', back_populates='product_types')
    products = relationship('Product', back_populates='type')

    __table_args__ = (
        UniqueConstraint('category_id', 'title', name='category_title'),
    )