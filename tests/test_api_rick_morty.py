import json
from http import HTTPStatus
import allure

from qa_automation_hw.api_cpllections.episode_api import EpisodeAPI
from qa_automation_hw.api_cpllections.locations_api import LocationAPI
from qa_automation_hw.api_cpllections.people_api import PeopleApi
from qa_automation_hw.data_classes.person import Person


@allure.feature('Nazar Sennyk')
def test_get_character(env):
    response = PeopleApi(env).get_person_by_id(1)
    assert response.status_code == HTTPStatus.OK, 'Not 200 status code'


@allure.feature('Nazar Sennyk')
def test_response_body(crate_person, env):
    expected_person = crate_person
    response = PeopleApi(env).get_person_by_id(1)
    from_json = json.loads(response.text)
    actual_person = Person.create_from_json(**from_json)
    assert actual_person == expected_person


@allure.feature('Nazar Sennyk')
def test_create_person(env):
    response = PeopleApi(env).create_person(
        body={"id": 999, "name": "Darth Vader", "status": "Alive", "species": "Jedi",
              "type": "", "gender": "Male", "origin": {"name": "unknown", "url": ""},
              "location": {"name": "Interdimensional Cable",
                           "url": "https://rickandmortyapi.com/api/location/6"},
              "image": "https://rickandmortyapi.com/api/character/avatar/275.jpeg",
              "episode": ["https://rickandmortyapi.com/api/episode/19"],
              "url": "https://rickandmortyapi.com/api/character/275",
              "created": "2022-12-31T14:16:45.776Z"})
    assert response.status_code == HTTPStatus.OK, 'Not 200 status code'


@allure.feature('Nazar Sennyk')
def test_get_episode(env):
    response = EpisodeAPI(env).get_episode_id(15)
    assert response.status_code == HTTPStatus.OK, 'Not 200 status code'


@allure.feature('Nazar Sennyk')
def test_get_location_id(env):
    response = LocationAPI(env).get_location_id(9)
    assert response.status_code == HTTPStatus.OK, 'Not 200 status code'


@allure.feature('Nazar Sennyk')
def test_random_person(env):
    response = PeopleApi(env).get_random_person_by_id()
    print(response.text)
    assert response.status_code == HTTPStatus.OK, 'Not 200 status code'
