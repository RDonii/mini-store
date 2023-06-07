import enum
from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class CurrencyEnum(enum.Enum):
    UZS = 'UZS'
    USD = 'USD'


class Product(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    model = Column(String, index=True)
    unit_cost = Column(DECIMAL(7, 2), nullable=False)
    unit_price = Column(DECIMAL(7, 2), nullable=False)
    currency = Column(Enum(CurrencyEnum), default=CurrencyEnum.UZS)
    amount = Column(Integer, default=0)
    type_id = Column(Integer, ForeignKey('product_type.id'), nullable=False)
    type = relationship('ProductType', back_populates='products')
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())
