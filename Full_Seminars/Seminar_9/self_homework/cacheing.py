'''
Задача 4. Кэширование для ускорения вычислений
Создайте декоратор, который кэширует (сохраняет для дальнейшего использования)
результаты вызова функции и, при повторном вызове с теми же аргументами,
возвращает сохранённый результат.
Примените его к рекурсивной функции вычисления чисел Фибоначчи.
В итоге декоратор должен проверять аргументы, с которыми вызывается функция, и,
если такие аргументы уже использовались, должен вернуть сохранённый результат
вместо запуска расчёта.
'''

from functools import wraps
from typing import Callable

def cache_dec(func: Callable):
    cache = {}

    @wraps(func)
    def wrapper(num):
        if num in cache:
            return cache[num]
        result = func(num)
        cache[num] = result
        print(cache)
        return result

    return wrapper

def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == '__main__':
    fib_cache = cache_dec(fibonacci)

    print(fib_cache(10))  # 55
    print(fib_cache(10))  # 55 (cached)
    print(fib_cache(15))
    print(fib_cache(11))
    print(fib_cache(15))  # 610 (cached)