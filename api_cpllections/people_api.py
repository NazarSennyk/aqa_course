import random
from qa_automation_hw.data_classes.peson import Person
from qa_automation_hw.utilities.api.BaseAPI import BaseAPI


class PeopleApi(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__url = 'api/character/'
        self.__url_episode = 'api/episode'
        self.__location = 'api/location/'
        self.__random_person = random.randint(1, 99)

    def get_person_by_id(self, person_id: int, headers=None):
        return self.get(f'{self.__url}/{person_id}', headers=headers)

    def create_person(self, body=None):
        person_data = Person()
        if body is not None:
            person_data.update_dict(**body)
        response = self.post(self.__url, body=person_data.get_json())
        return response

    def get_episode_id(self, episode_id: int):
        return self.get(f'{self.__url_episode}/{episode_id}')

    def get_location_id(self, location_id: int):
        return self.get(f'{self.__location}/{location_id}')

    def get_random_person_by_id(self):
        return self.get(f'{self.__url}/{self.__random_person}')
