import collections
import pprint
import os


def my_print(some_function):
    return os.system(f'echo {some_function()}')


def letter_frequency():
    with open('text.txt') as file:
        count = collections.Counter(file.read().lower())
        value = pprint.pformat(count)
        return value.split(',')

my_print(some_function)








