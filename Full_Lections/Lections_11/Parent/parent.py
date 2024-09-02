'''
Задание 1. Отцы, матери и дети.
Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
● имя,
● возраст,
● список детей.
И он может:
● сообщить информацию о себе,
● успокоить ребёнка,
● покормить ребёнка.
У ребёнка есть:
● имя,
● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
● состояние спокойствия,
● состояние голода.
Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
и словарь состояний, и что-то поинтереснее.
'''
class Parent:
    def __init__(self, name, age, children_list):
        self.name = name
        self.age = age
        self.children_list = []

    def __repr__(self):
        return f'Класс семьи, состоящей из родителя отца {self.name}, возраст {self.age} и его ребенка\детей {self.children_list}'
    def add_child(self, child):
        """Добавляет ребёнка в список детей, если разница в возрасте
        больше 16 лет"""
        if self.age - child.age >= 16:
            self.children_list.append(child)
            print(f"Ребёнок {child.name} добавлен к {self.name}.")
        else:
            print(f"Ребёнок {child.name} не добавлен к {self.name},так как разница в возрасте слишком мала.")

    def info(self):
        return f'Меня зовут {self.name}, мне {self.age}'

    def feed_child(self, child_name):
        if child_name in self.children_list:
            child_name.hungry = False
            print(f'Покормлен ребёнок {child_name}.')
        else:
            print(f'Ребёнка {child_name} не найден.')

    def list_of_children(self):
        if self.children_list:
            print(f'У {self.name} есть след дети: ')
            for child in self.children_list:
                print(f'{child.name}, {child.age}')

    def calm_child(self, child_name):
        if child_name in self.children_list:
            child_name.calm = True
            print(f'Ребёнок {child_name} успокоен.')
        else:
            child_name.calm = False
            print(f'Ребёнок {child_name} не успокоен.')


class Child(Parent):
    '''У ребёнка есть:
● имя,
● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
● состояние спокойствия,
● состояние голода.
'''
    max_happiness = 10
    medium_happiness = 5
    not_happiness = 0
    def __init__(self, name, age, happiness):
        super().__init__(name, age, children_list=None)
        self.happiness = happiness

    def control_age(self, other):
        if other.age > self.age + 16:
            print('Возраст соответствует')
        else:
            print('Слишком молод')

    def child_happiness(self):
        if 0 < self.happiness < 10:
            self.happiness = self.medium_happiness
            print(f'Ребенок счастлив, уровень счастья = {self.medium_happiness} ')
        elif self.happiness == 10:
            self.happiness = self.max_happiness
            print(f'Ребенок очень счастлив, уровень счастья = {self.max_happiness} ')
        else:
            print(f'Ребенок не счастлив, уровень счастья = {self.not_happiness} ')

if __name__ == '__main__':
    parent = Parent('Иван', 40, [])
    child = Child('Мария', 20, 5)
    child2 = Child('Петр', 20, 5)
    parent.add_child(child)
    parent.add_child(child2)
    parent.info()
    parent.feed_child('Мария')
    parent.list_of_children()
    child.child_happiness()
    child.control_age(parent)