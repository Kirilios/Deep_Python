"""
Задание №4
📌 Создайте класс Сотрудник.
📌 Воспользуйтесь классом человека из прошлого задания.
📌 У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
"""


class Person:

    def __init__(self, name: str, age: int, phone: str):
        self.__name = name
        self.__age = age
        self.__phone = phone

    def birthday(self):
        self.__age += 1

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Employee(Person):

    def __init__(self, name: str, age: int, phone: str, id: int):
        super().__init__(name, age, phone)
        self.__id = id
        self.__level = id % 7

    def info(self):
        return f"{self.__id} : ({self.__level}) {self.name} / {self.age} / {self.phone}"


e = Employee("Иван", 33, "1-234-567-8901", 123456)
print(e.info())