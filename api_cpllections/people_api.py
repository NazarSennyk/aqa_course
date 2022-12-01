from qa_automation_hw.utilities.api.BaseAPI import BaseAPI


class PeopleApi(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = '/character'

    def get_person_by_id(self, person_id, headers=None):
        return self.get(f'{self.__url}/{person_id}', headers=headers)
