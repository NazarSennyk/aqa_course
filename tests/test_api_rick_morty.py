import json
from http import HTTPStatus
from qa_automation_hw.api_cpllections.people_api import PeopleApi
from qa_automation_hw.data_classes.peson import Person


def test_get_character(env):
	response = PeopleApi(env).get_person_by_id(1)
	assert response.status_code == HTTPStatus.OK, 'Not 200 status code'


def test_response_body(crate_person, env):
	expected_person = crate_person
	response = PeopleApi(env).get_person_by_id(1)
	from_json = json.loads(response.text)
	actual_person = Person.create_from_json(**from_json)
	assert actual_person == expected_person


def test_create_person(env):
	response = PeopleApi(env).create_person(body={'origin':'{"name":"Earth (C-137)","url":"https://rickandmortyapi.com/api/location/1"}'})


def test_get_episode(env):
	response = PeopleApi(env).get_episode_id(15)
	assert response.status_code == HTTPStatus.OK, 'Not 200 status code'


def test_get_location_id(env):
	response = PeopleApi(env).get_location_id(9)
	assert response.status_code == HTTPStatus.OK, 'Not 200 status code'


def test_random_person(env):
	response = PeopleApi(env).get_random_person_by_id()
	print(response.text)
	assert response.status_code == HTTPStatus.OK, 'Not 200 status code'
