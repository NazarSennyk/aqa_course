import collections
import pprint
import os


def my_print():
    "Don't know how to do from received materials don't see the solutions"


def letter_frequency():
    with open('text.txt') as file:
        count = collections.Counter(file.read().lower())
        value = pprint.pformat(count)
        return value









