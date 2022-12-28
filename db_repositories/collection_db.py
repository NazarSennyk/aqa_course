from db_repositories.baseDB import BaseDb


class Collection(BaseDb):
    def __init__(self):
        super().__init__()

    def insert_one(self, brand: str, engine: float, year: int):
        self.mycol.insert_one({'brand': f'{brand}', 'engine': f'{engine}', 'year': f'{year}'})

    def insert_many(self, brand: str, engine: float, year: int):
        self.mycol.insert_many([{'brand': f'{brand}', 'engine': f'{engine}', 'year': f'{year}'},
                                {'brand': f'{brand}', 'engine': f'{engine}', 'year': f'{year}'}])



Collection().insert_one('Mercedes', 2.0, 2020)
Collection().insert_many('BMW', 3.0, 2021, 'Aston Martin', 5.0, 2022)
Collection().find_car_by_engine(3.0)
Collection().find_all()
Collection().update_car_info('Volvo')
