"""
Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
"""

import json
import math


# def save_to_json(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         filename = func.__name__ + '.json'
#         data = {}
#         data['args'] = args
#         data['kwargs'] = kwargs
#         data['result'] = result
#
#     try:
#         with open(filename, 'a', encoding='utf-8') as f:
#             try:
#                 existing_data = json.load(f)
#             except json.JSONDecodeError:
#                 existing_data = []
#
#             existing_data.append(data)
#             f.seek(0)
#             json.dump(existing_data, f, indent=4)
#         except FileNotFoundError:
#             with open(filename, 'w', encoding='utf-8') as f:
#                 json.dump([data], f, indent=4)
#
#         return result
#
#     return wrapper
#
# @save_to_json
# def my_function(a, b, c=3):
#     return a + b + c
#
# my_function(1, 2)
# my_function(3, 4, c=5)
#
# if __name__ == "__main__":
#     with open('my_function.json', encoding='utf-8') as f:
#         print(f.read())

# option2
from json import dump


def decorator(func):
    my_dict = {}

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        file_name = f'{func.__name__}.json'
        my_dict['args'] = f'{args[0]}, {args[1]}'
        for k, v in my_dict.items():
            my_dict[k] = v
        my_dict['res'] = res
        with open(file_name, 'a', encoding="utf-8") as js_f:
            dump(my_dict, js_f, indent=2)
        return res

    return wrapper

@decorator
def func(a, b):
    return pow(a, b)


print(func(2, 5))