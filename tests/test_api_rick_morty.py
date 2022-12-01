import pytest
import requests
from http import HTTPStatus
from qa_automation_hw.api_cpllections.people_api import PeopleApi


def test_get_character(env):
	response = PeopleApi().get_person_by_id(1)
	assert response.status_code == HTTPStatus.OK, 'Not 200 status code'

