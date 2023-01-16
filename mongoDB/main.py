from mongoDB.objects.products_db import Products

more_data = [{"product_name": "rice", "bulk_weight_kg": 1, "price_per_kg": 30},
             {"product_name": "spaghetti", "bulk_weight_kg": 1, "price_per_kg": 50},
             {"product_name": "milk", "bulk_volume_L": 1, "price_per_l": 30},
             {"product_name": "ketchup", "bulk_volume_L": 1, "price_per_l": 80}]

products = Products()
list_kg = ["Apples", 40, 30]
list_litre = ["Cola", 30, 35]
products.insert_many_in_db(more_data)
products.insert_one_in_kg(list_kg)
products.insert_one_in_l(list_litre)
products.find_all()
products.delete_by_dict({"product_name": "Apples"})
products.find_all()
products.delete_many_by_dict({"product_name": "Apples"})
products.delete_many_by_dict({"product_name": "Cola"})
products.find_all()
products.update_one_in_db({"product_name": "rice"}, {"bulk_weight_kg": 20})
products.find_all()
