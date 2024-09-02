"""
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circle_length(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    circle = Circle(10)

    circle_length = circle.get_circle_length()
    print("Длина окружности:", circle_length)

    area = circle.get_area()
    print("Площадь окружности:", area)
