

res = foo(1, 2)

res = foo('sdfg', 2)


def type_checker(arg_type):
     print('type_checker', arg_type)

     def outer_decorator(func):

         def inner_decorator(*args, **kwargs):
             print('decorator inner_decorator')
             for arg in args:
                 if not isinstance(arg, arg_type):
                     raise TypeError(f'Wrong arg type {type(arg)}')

             for k, v in kwargs:
                 if not isinstance(v, arg_type):
                     raise TypeError(f'Wrong kwarg type {k} {type(v)}')

             res = func(*args, **kwargs)

             print('decorator inner_decorator')
             return res

         return inner_decorator

     return outer_decorator