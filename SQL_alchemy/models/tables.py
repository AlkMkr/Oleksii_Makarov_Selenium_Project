from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, VARCHAR, INTEGER, ForeignKey

from SQL_alchemy.session import engine

Base = declarative_base()


class Products(Base):
    __tablename__ = "products"
    id = Column(INTEGER, primary_key=True)
    product_name = Column(VARCHAR(25), nullable=False)
    price = Column(INTEGER, nullable=False)

    def __str__(self):
        return f'id: {self.id}, product_name: {self.product_name}, price: {self.price}'


class Orders(Base):
    __tablename__ = "orders"
    id = Column(INTEGER, primary_key=True)
    product_id = Column(INTEGER, ForeignKey("products.id"))
    quantity = Column(INTEGER, nullable=False)

    def __str__(self):
        return f'id: {self.id}, product_id: {self.product_id}, quantity: {self.quantity}'


# This one creates tables
Base.metadata.create_all(engine)
