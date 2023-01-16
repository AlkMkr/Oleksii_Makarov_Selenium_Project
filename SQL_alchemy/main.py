from SQL_alchemy.models.tables import Products, Orders
from SQL_alchemy.repositories.products_repository import ProductsRepository

product_repo = ProductsRepository()
# I am going with naive approach and just dump everything here
product1 = Products(product_name='Lays', price=40)
product2 = Products(product_name='Tuna', price=150)
product3 = Products(product_name='Tomato', price=80)
product4 = Products(product_name='Beef', price=100)
product5 = Products(product_name='Juice', price=40)

if product_repo.get_max_id_products() < 7:
    product_repo.insert_product([product1, product2, product3, product4, product5])

order1 = Orders(product_id='2', quantity=30)
order2 = Orders(product_id='1', quantity=20)
order3 = Orders(product_id='3', quantity=40)
order4 = Orders(product_id='6', quantity=110)
order5 = Orders(product_id='5', quantity=40)
order6 = Orders(product_id='4', quantity=10)
if product_repo.get_max_id_orders() < 7:
    product_repo.insert_order([order1, order2, order3, order4, order5, order6])

products = product_repo.get_homework()
