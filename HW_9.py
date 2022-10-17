# напишіть функцію, яка перевірить, чи передане їй число є парним чи непарним (повертає True False)
# напишіть функцію. яка приймає стрічку, і визначає, чи дана стрічка відповідає результатам роботи методу capitalize() (перший символ є верхнім регістром, а решта – нижнім.)
# (повертає True False)
# написати до кожної функції мінімум 5 assert
# написати декоратор, який добавляє принт з результатом роботи отриманої функції + текстовий параметр, отриманий ним (декоратор з параметром - це там, де три функції)
# при цьому очікувані результати роботи функції не змінюються (декоратор просто добавляє принт)
def decor_print_result(func):
    """
    :param func: function
    :return: printed result of function in args
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return print(str(wrapper()), """
    :param func: function
    :return: printed result of function in args
    """)
@decor_print_result
def odd_check(integer):
    """
    :param integer: int
    :return: True if integer % 2 == 0 else return False
    """
    if integer % 2 == 1:
        return False
    if integer % 2 == 0:
        return True
assert type(odd_check(' ')) is True, 'Error'
assert odd_check(1.54) is True, 'Error'
assert odd_check('sdsa') is True, 'Error'
assert odd_check() is True, 'Error'
assert odd_check(' 353') is True,'Error'
@decor_print_result
def capitalize_check(arg):
    """
    Function checks if given arg is .capitalize()
    :param arg string
    :return: True if string == .capitalize() else return False
    """
    if arg == arg.capitalize():
        return True
    else:
        return False
assert capitalize_check('12345') is True, 'Error'
assert capitalize_check(54353) is True, 'Error'
assert capitalize_check('sdada') is True, 'Error'
assert capitalize_check('  ') is True, 'Error'
assert capitalize_check('   fdfddAsad') is True,'Error'


