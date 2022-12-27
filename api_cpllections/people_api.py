import random
from data_classes.person import Person
from utilities.api.BaseAPI import BaseAPI


class PeopleApi(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__url = 'api/character/'
        self.__random_person = random.randint(1, 99)

    def get_person_by_id(self, person_id: int, headers=None):
        return self.get(f'{self.__url}/{person_id}', headers=headers)

    def create_person(self, body=None):
        person_data = Person()
        if body is not None:
            person_data.update_dict(**body)
        response = self.post(self.__url, body=person_data.get_json())
        return response

    def get_random_person_by_id(self):
        return self.get(f'{self.__url}/{self.__random_person}')
