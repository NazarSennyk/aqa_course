import requests
from pprint import pprint


url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
response_json = response.json()
people = response_json['people']
name = 'name'
people = [b_dict[name] for b_dict in people]
for person in people:
    pprint(person, width=200)