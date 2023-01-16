from sqlalchemy.sql import label

from SQL_alchemy.models.tables import Products, Orders
from SQL_alchemy.session import session
from sqlalchemy import func


class ProductsRepository:
    def __init__(self):
        self.__session = session

    def insert_product(self, products: list):
        """
            Insert into table Products
        """
        self.__session.add_all(products)

    def insert_order(self, orders: list):
        """
            Insert into table Orders
        """
        self.__session.add_all(orders)

    def get_homework(self):
        """
            Makes an inner Join returning product id, product name, price, quantity and total price.
        """
        homework = self.__session.query(Products.id, Products.product_name, Products.price, Orders.quantity,
                                        (label('total', Products.price * Orders.quantity))).join(Orders)
        for item in homework:
            print(
                f'product_id:{item[0]}, product_name:{item[1]}, price:{item[2]}, quantity: {item[3]}, total:{item[4]}')

    def get_max_id_products(self):
        """
            Returns max id in Products table
        """
        max_id = self.__session.query(func.max(Products.id)).scalar()
        return max_id

    def get_max_id_orders(self):
        """
            Returns max id in Orders table
        """
        max_id = self.__session.query(func.max(Orders.id)).scalar()
        return max_id
