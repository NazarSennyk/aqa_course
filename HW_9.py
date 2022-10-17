
def decor_print_result(func):
    """
    :param func: function
    :return: printed result of function in args
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return print((str(wrapper(4))), """
    :param func: function
    :return: printed result of function in args
    """)
@decor_print_result
def odd_check(integer):
    """
    :param integer: int
    :return: True if integer % 2 == 0 else return False
    """
    if type(integer) is int and float and integer % 2 == 0:
        return True
    else:
        return False
assert odd_check('str') is False, 'Error'
assert odd_check(1.54) is False, 'Error'
assert odd_check(100) is True, 'Error'
assert odd_check(-10) is True, 'Error'
assert odd_check(' ') is False, 'Error'
@decor_print_result
def capitalize_check(arg):
    """
    Function checks if given arg is .capitalize()
    :param arg string
    :return: True if string == .capitalize() else return False
    """
    res = True if arg == str(arg).capitalize() else False
    return res
assert capitalize_check('dadas') is False, 'Error'
assert capitalize_check(54353) is False, 'Error'
assert capitalize_check('234') is True, 'Error'
assert capitalize_check('  ') is True, 'Error'
assert capitalize_check('Rd322ffA') is False,'Error'


