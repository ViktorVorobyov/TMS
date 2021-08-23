rom datetime import datetime

from sqlalchemy import Integer, String, Column, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)

    purchases = relationship("Purchase", back_populates="user")


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    purchases = relationship("Purchase", back_populates="product")


class Purchase(Base):
    __tablename__ = "purchase"
    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="purchases")

    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    product = relationship("Product", back_populates="purchases")