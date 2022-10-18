def decorator(arg):
    def decor_print_result(func):
        """ Returns printed result of function in it
        :param func: function
        :return: printed result of function in args
        """
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(func)
            return result
        return wrapper
    return decor_print_result


@decorator('Function that checks if given argument is even or not')
def odd_check(integer_float):
    """
    Function that checks if given argument is even or not
    :return: True if argument % 2 == 0 else return False
    """
    if integer_float % 2 == 0:
        return True
    else:
        return False


assert odd_check(3) is False
assert odd_check(1.54) is False
assert odd_check(100) is True
assert odd_check(-10) is True
assert odd_check(0.213) is False


@decorator('Function checks if given arg starts with capitalize letter')
def capitalize_check(arg):
    """
    Function checks if given arg starts with capitalize letter
    :param arg string
    :return: True if string == .capitalize() else return False
    """
    if arg == arg.capitalize():
        return True
    else:
        return False


assert capitalize_check('dadas') is False
assert capitalize_check('234') is True
assert capitalize_check('  ') is True
assert capitalize_check('Rd322ffA') is False
assert capitalize_check('23.45') is True

