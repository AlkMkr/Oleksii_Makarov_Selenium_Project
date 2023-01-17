import pymongo


class BaseDB:
    def __init__(self, database, collection):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client[database]
        self.collection = self.database[collection]

    def _insert_one_in_db(self, data: dict):
        """
            A method to insert one dict in collection
        """
        self.collection.insert_one(data)

    def insert_many_in_db(self, data: list):
        """
            A method to insert many dicts in collection. Should be a list of dictionaries.
        """
        self.collection.insert_many(data)

    def update_one_in_db(self, subject: dict, values: dict):
        """
            A method to update one value in collection.
            Subject: a value to be updated.
            Values: new value.
        """
        self.collection.update_one(subject, {"$set": values})

    def find_all(self):
        """
            A method that finds all values in a collection
        """
        result = self.collection.find()
        for i in result:
            print(i)

    def _find_all_without_id(self, data: dict):
        """
            A method that finds all values in a collection without showing id
        """
        result = self.collection.find({}, {data})
        for i in result:
            print(i)

    def find_by_dict(self, data: dict):
        """
            A method to find object in collection by value.
        """
        result = self.collection.find(data)
        for i in result:
            print(i)

    def delete_by_dict(self, data: dict):
        """
            A method to delete one object based on a dict.
        """
        self.collection.delete_one(data)

    def delete_many_by_dict(self, data: dict):
        """
            A method to delete all objects based on a dict.
        """
        result = self.collection.delete_many(data)
        if result.deleted_count == 1:
            print(f'{result.deleted_count} object was deleted')
        else:
            print(f'{result.deleted_count} objects were deleted')
