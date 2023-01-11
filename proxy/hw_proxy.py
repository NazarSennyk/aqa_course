import collections
import pprint
import os


def my_print():
    for item in os.scandir('.'):
        temp_item: os.DirEntry = item
        print(f'{temp_item.path}')
        with open('text.txt') as file:
            count = collections.Counter(file.read().lower())
            value = pprint.pformat(count)
            return print(value)


my_print()











