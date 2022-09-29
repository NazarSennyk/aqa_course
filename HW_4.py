# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Зауважте, що lst1 не є статичним і може формуватися динамічно.
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for element in lst1:
    if type(element) == str:
        lst2 = lst2.append(element)
        lst2 = element.split(',')
        print(lst2)
lst2 = lst2.remove('Lorem Ipsum')    #Для чого ця дія-> чомусь в мому лісті додавалось додаткова стрінга 'Lorem Ipsum'
print(lst2)                          # і воно на виході робило дубель її, я додатково її стер, знаю шо не дуже, по іншому не знав як


# Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
# Напишіть код, який видалить з нього всі числа, які менше 21 і більше 74.
lst3 = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]
for elem in lst3:
    if elem < 21:
        lst3.remove(elem)
    if elem > 74:
        lst3.remove(elem)
print(lst3)

# 3----Є стрінг з певним текстом (можна скористатися input або константою).
# Напишіть код, який визначить кількість слів в цьому тексті, які закінчуються на 'о'.


while True:
    user_input = input('Please enter a word that ends with \'O\' letter:').lower()
    user_input.split()
    counter = 0
    for word in user_input:
        if word.endswith('o'):
            counter += 1
    print(f' Yor words: {user_input} it has {counter} words with \'O\' in the end ')
    break
