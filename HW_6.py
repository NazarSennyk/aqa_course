
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
while True:
    for person in response_json:
        pprint(people, width=200)
        time.sleep(5)




#2.роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране
url = 'https://api.openweathermap.org/data/2.5/weather?q=lviv&appid=47503e85fabbabc93cff28c52398ae97&units=metric'
response = requests.get(url)
response_json = response.json()
weather = response_json['main']
wind = response_json['wind']
while True:
    for data in weather:
        print('Lviv\'s temperature is :', weather['temp'])
        print('Lviv\'s wind speed is:', wind['speed'])
        time.sleep(8)
