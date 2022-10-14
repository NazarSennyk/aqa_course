# # Напишіть декоратор, який перетворює результат роботи функції на стрінг
# # Напишіть докстрінг для цього декоратора
def outer_decorator(func):
    """This decorator transforms data from other function in to a str """
    def inner_decorator(*args,**kwargs):
        result = str(func(*args))
        return result
    return inner_decorator

@outer_decorator
def input_in_list():
    user_input = list(input('Please enter something:'))
    return user_input
result = input_in_list()
print(type(result))

