"""
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""

def decorator(param):
    def real_decor(func):
        def wrapper(*args, **kwargs):
            count = 0
            for _ in range(param):
                res = func(args[0], args[1])
                count += 1
            return res, count
        return wrapper
    return real_decor


@decorator(10)
def func(a, b):
    return pow(a, b)

print(func(2,4))

# print(decorator(10)(func)(2,5))