import re
from pprint import pprint
# # Task_1
# json_dict = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
#
# def convert_name1(name: str):
#     result1 = re.compile('[\w]+=\w+')
#     result2 = result1.findall(name)
#     final_dict = {}
#     for item in result2:
#         temp = item.split('=')
#         final_dict[temp[0]] = temp[1]
#     return final_dict
#
#
# print(convert_name1(json_dict))
#
# # Task_2
# words = '["FirstItem", "FriendsList", "MyTuple"]'
#
#
# def convert_name2(name: str):
#     s1 = re.sub('(.)([A-Z][a-z]+)', r'\1\2', name).replace('[', '')
#     return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower().replace('"','').replace(']','').split(', ')
#
#
# print(convert_name2(words))
#
# # Tesk_3

def regex_for_txt():
    with open('text.txt') as file:
        var_file = file.read()
        regex = re.compile("\W\s")
        regex_result = regex.sub(' ', var_file)
        new_str = str(regex_result)
        return new_str

pprint(regex_for_txt())

