import pymongo


class BaseDb:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = client['cars']
        self.mycol = mydb['cars_list']

    def insert_one(self, brand: str, engine: float, year: int):
        self.mycol.insert_one({'brand': f'{brand}', 'engine': f'{engine}', 'year': f'{year}'})

    def insert_many(self, brand: str, engine: float, year: int):
        self.mycol.insert_many([{'brand': f'{brand}', 'engine': f'{engine}', 'year': f'{year}'},
                                {'brand': f'{brand}', 'engine': f'{engine}', 'year': f'{year}'}])

    def find_all(self):
        result = self.mydb.mycol.find({})
        return result

    def find_car_by_engine(self, engine: float):
        result = self.mydb.mycol.find({'engine': f'{engine}'})
        return result
