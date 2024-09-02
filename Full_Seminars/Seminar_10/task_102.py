"""
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""

class Rectangle:

    def __init__(self, *args):
        if len(args) == 1:
            self.__length = args[0]
            self.__width = args[0]
        elif len(args) == 2:
            self.__length = args[0]
            self.__width = args[1]

    def get_perimeter(self):
        return 2 * (self.__width + self.__length)

    def get_square(self):
        return self.__length * self.__width


r_1 = Rectangle(2, 3)
r_2 = Rectangle(4)
print(f"{r_1.get_perimeter() = } {r_1.get_square() = }")
print(f"{r_2.get_perimeter() = } {r_2.get_square() = }")