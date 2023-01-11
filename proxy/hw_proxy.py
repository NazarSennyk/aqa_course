import collections
import pprint
import os


def my_print():
    return os.system(f'echo {letter_frequency()}')


def letter_frequency():
    with open('text.txt') as file:
        count = collections.Counter(file.read().lower())
        value = pprint.pformat(count)
        return value.split(',')

my_print()








