from api.BaseAPI import BaseAPI


class LocationAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__location = 'api/location/'

    def get_location_id(self, location_id: int):
        return self.get(f'{self.__location}/{location_id}')
