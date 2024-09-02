'''
Задача 2. Замедление кода
В программировании иногда возникает ситуация, когда работу функции нужно
замедлить. Типичный пример — функция, которая постоянно проверяет,
изменились ли данные на веб-странице или её код.
Реализуйте декоратор, который перед выполнением декорируемой функции
ждёт несколько секунд.
'''
from functools import wraps
import time
from typing import Callable


def delay_decorator(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Время начала: {time.time():0.2f}')
        time.sleep(5) # Замедляем выполнение на 5 секунд
        print(f'Время конца: {time.time():0.2f}')
        result = func(*args, **kwargs)
        return result
    return wrapper

@delay_decorator
def testing():
    print('Замедление сработало')

if __name__ == '__main__':
    testing()
