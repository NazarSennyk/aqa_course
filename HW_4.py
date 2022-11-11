test_list = [
    {'Course': "C++", 'Author': "Jerry"},
    {'Course': "Python", 'Author': "Mark"},
    {'Course': "Java", 'Author': "Paul"}]

# Find dictionary matching value in list
res = next((sub for sub in test_list if sub['Course'] == "Java"), None)

# printing result
print("The filtered dictionary value is : " + str(res))