# Зформуйте строку, яка містить певну інформацію про символ в відомому слові. Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".
user_word = input('Enter your word:')
user_symbol = input('Enter your symbol:')
if user_symbol == str(user_symbol):
    print('Enter letter')
else:
    user_symbol = int(user_symbol)
    resualt = user_word[user_symbol]
    print(f' "The {user_symbol} symbol in \'{user_word}\' is \'{resualt}\' "')

#Написати цикл, який буде вимагати від користувача ввести слово, в якому є буква "о" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви о.
while True:
    user_input = input("Enter the word that contains 'o' upper case or lower cases:")
    if 'o' in user_input.lower() or 'o' in user_input.upper():
        print(f'Thanks for {user_input}!')
        break
    if user_input.isdigit():
        print('You must  enter a word not a digit')
        continue
    if user_input is not str or int:
        print('You entered not valid data')
        continue

