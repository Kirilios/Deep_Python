'''
Задача 3. Счётчик
Реализуйте декоратор counter, считающий и выводящий количество вызовов
декорируемой функции.
'''
from typing import Callable


def decorator(func: Callable):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f'Функция {func.__name__} вызвана {wrapper.calls} раз(а)')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        return result
    wrapper.calls = 0
    return wrapper


@decorator
def greetings(name, age):
    if age:
        return f'Привет, {name}! Тебе {age} лет.'
    else:
        return f'Привет, {name}!'

@decorator
def greetings2(name):
    return f'Привет, {name}!'


if __name__ == '__main__':
    greetings("Кирилл", '7')
    greetings('Semen', 14)
    greetings2("Алексей")