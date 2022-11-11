
#Дана довільна строка.
#Напишіть код, який знайде в ній і виведе на екран кількість слів, які містять дві голосні літери підряд.

user_input = input("WORD:-> ").lower()
vowels = ['a', 'e', 'i', 'o', 'u', 'y', ]
vowel_count = 0

for word in user_input.split():
    word_vow = 0
    for vowel in word:
        word_vow = word_vow + 1 if vowel in vowels else 0
        if word_vow == 2:
            vowel_count += 1
            break
print(vowel_count)


#Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
#{ "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "sota": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.
#Наприклад: > match: "x-store", "main-service"
#lower_limit = 35.9
#upper_limit = 37.339

# shops_price = {
#           "cito": 47.999,
#           "BB_studio": 42.999,
#           "momo": 49.999,
#           "main-service": 37.245,
#           "buy.now": 38.324,
#           "x-store": 37.166,
#           "the_partner": 38.988,
#           "sota": 37.720,
#           "rozetka": 38.003
#                }
# lower_limit = 38.002
# upper_limit = 42.999
# for key, value in shops_price.items():
#     if lower_limit <= value <= upper_limit:
#         print(key, value)
