from qa_automation_hw.db_repositories.baseDB import BaseDb


class Collection(BaseDb):
    def __init__(self):
        super().__init__()

    def update_car_info(self, brand_name):
        self.mydb.mycol.updateOne({ brand: 'Mercedes', { $set: { brand: f'{brand_name}' }})





Collection().insert_one('Mercedes', 2.0, 2020)
Collection().insert_many('BMW', 3.0, 2021, 'Aston Martin', 5.0, 2022)
Collection().find_car_by_engine(3.0)
Collection().find_all()
Collection().update_car_info('Volvo')
