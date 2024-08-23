from typing import Callable

# def add_one_str(a: str) -> Callable[[str], str]:
#     names = []
#
#     def add_two_str(b: str) -> str:
#         names.append(b)
#         return  a + ', ' + ', '.join(names)
#
#     return add_two_str
#
# hello = add_one_str("Hello")
# bye = add_one_str('Good bye')
#
# print(hello('Kirill'))
# print(hello('Nikita'))
# print(bye('Vanya'))

#неизменяемые типы

# def add_one_str(a: str) -> Callable[[str], str]:
#     text = ''
#
#     def add_two_str(b: str) -> str:
#         nonlocal text
#         text += ', ' + b
#         return  a + text
#
#     return add_two_str
#
# hello = add_one_str("Hello")
# bye = add_one_str('Good bye')
#
# print(hello('Pavel'))
# print(hello('Edick'))
# print(hello('Nikita'))
# print(bye('Vanya'))
# print(bye('Vanya2'))

import random

def cache(func: Callable):
    _cache_dict = {}

    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]
    return wrapper

@cache
def rnd(a: int, b: int):
    print('start')
    return random.randint(a, b)


print(f'{rnd(1,10) = }')
print(f'{rnd(1,10) = }')
print(f'{rnd(1,10) = }')

## decorator with parameters
'''
def count(param):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
        …

            return result

    return wrapper

return deco
'''