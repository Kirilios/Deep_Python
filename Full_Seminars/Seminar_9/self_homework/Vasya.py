'''
Задание 1. Как дела?
Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
написал надоедливый декоратор, который при вызове декорируемой функции
спрашивает у пользователя «Как дела?», вне зависимости от ответа пишет что-то
вроде «А у меня не очень!» и только потом запускает саму функцию. Правда, после
такой выходки Васю чуть не уволили с работы
'''

import functools
from typing import Callable


def greeting_decorator(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        input("Как дела? ")
        print('А у меня не очень. Держи свое функцию')
        result = func(*args, **kwargs)
        return result
    return wrapper

@greeting_decorator
def func():
    print("я работаю")

if __name__ == '__main__':
    func()