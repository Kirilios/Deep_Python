'''

Напишите функцию key_params,
принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
На входе:
params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
На выходе:
{1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
'''


def key_params(**kwargs):
    dict1 = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, frozenset, bytearray)):
            value = str(value)
        dict1[value] = key
    return dict1


params = key_params(a=None, b='', c=[], d ={})
print(params)
