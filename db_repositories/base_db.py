import pymongo


class BaseDb:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = client['cars']
        self.mycol = mydb['cars_list']

    def find_all(self):
        result = self.mydb.mycol.find({})
        return result

    def find_car_by_engine(self, engine: float):
        result = self.mydb.mycol.find({'engine': f'{engine}'})
        return result

    def update_car_info(self, brand_name):
        self.mydb.mycol.updateOne({ brand: 'Mercedes', { $set: { brand: f'{brand_name}' }})


