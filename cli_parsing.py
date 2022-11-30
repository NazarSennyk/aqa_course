import json
from argparse import ArgumentParser


class Human:
    def __init__(self, **kwargs):
        self.name = 'Dart Vader'
        self.age = 33
        self.gender = 'male'
        self.birth_year = 1989
        self.live_status = True
        self.special_weapone = None


jedi = Human()

parser = ArgumentParser(description='Parses to a json format')
parser.add_argument('--format', help='Parses to a json format', default='json')
args = parser.parse_args()


def convert_to_json():
    json_obj = json.dumps(jedi.__dict__)
    return json_obj


if args.format == 'json':
    result = convert_to_json()
    file = open('result.txt', 'w')
    file.write('%s = %s\n' % ('result', result))
    file.close()






