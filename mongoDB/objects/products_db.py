from mongoDB.objects.base_db import BaseDB


class Products(BaseDB):
    def __init__(self):
        super().__init__("store", "products")

    def insert_one_in_kg(self, values: list):
        """
            A method to insert one product with kg as units of measure. Takes list of values where:
            0 = Product_name
            1 = how much of kg there is
            2 = price per kg
        """
        self._insert_one_in_db(
            {"product_name": f"{values[0]}", "bulk_weight_kg": f"{values[1]}", "price_per_kg": f"{values[2]}"})

    def insert_one_in_l(self, values: list):
        """
            A method to insert one product with l as units of measure. Takes list of values where:
            0 = Product_name
            1 = how much of l there is
            2 = price per l
        """
        self._insert_one_in_db(
            {"product_name": f"{values[0]}", "bulk_volume_l": f"{values[1]}", "price_per_l": f"{values[2]}"})
