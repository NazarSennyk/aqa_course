#1. вивести список всіх астронавтів, що перебувають в даний момент на орбіті (дані не фейкові, оновлюються в режимі реального часу)
import requests
from pprint import pprint
import time

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
response_json = response.json()
people = response_json['people']
name = 'name'
people = [b_dict[name] for b_dict in people]
pprint(people, width=200)




#вивести список всіх астронавтів, що перебувають в даний момент на орбіті (дані не фейкові, оновлюються в режимі реального часу)

import requests

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
astros = response.json()

for astro in astros['people']:
    print(astro['name'])