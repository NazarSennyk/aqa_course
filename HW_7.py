

result = []
user_input = input('Введіть свій вік:')
def age_check():
    if int(user_input) % 10 == 1 and int(user_input) != 11:     #Запитав Василя як вивеести число з 21-го і збільшувати на 10, він мені це скинув, що і як воно робить не розумію нажаль.
        result.append('рік')
    elif user_input[-1] in ('2','3','4'):               #тут так і не знаю як зробити правильно, воно верівно виходить неправильно
        result.append('роки')
    else:
        result.append('років')








def user_data(result):
    if user_input.isdigit():
        age = int(user_input)
        if '7' in user_input:
            print("Вам сьогодні пощастить")
        elif age >= 190:
            print(f'Незважаючи на те, що вам {age} {result}, білетів всеодно нема!')
        elif age == 0:
            print(f'Незважаючи на те, що вам {age} {result}, білетів всеодно нема!')
        elif age < 16:
            print(f'Тобі лише {age} {result}, а це е фільм для дорослих!')
        elif age > 65:
            print(f'Вам {age} {result}? Покажіть пенсійне посвідчення!')
        else:
            print(f'Незважаючи на те, що вам {age} {result}, білетів всеодно нема!')
    else:
        print('Ви ввели неправильні дані')

age_check() ,user_data(result[0])