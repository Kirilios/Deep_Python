
class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, sex, race='unknown', speed=100):
        '''метод инит срабатывает при каждом создании экземпляра '''
        self.sex = sex
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self, num: int):
        if self._check_level():
            self.level += 1
        else:
            self.level = self._max_level

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)


# p1 = Person('Richard', 'm', 'Gnome')
# p2 = Person('Edward', 'm', 'Human')
# print(f'Твой персонаж: имя: {p1.name}, раса: {p1.race}, уровень: {p1.level}, здоровье: {p1.health}')
# p1.level_up(4)
# print(f'имя: {p1.name}, уровень: {p1.level}, здоровье: {p1.health}')
# p1.change_health(p2, 50)
# print(f'имя: {p1.name}, уровень: {p1.level}, здоровье: {p1.health}')
# print(f'имя: {p2.name}, уровень: {p2.level}, здоровье: {p2.health}')
# #help(__name__)

class Address:
    def __init__(self, country, city, street):
        self.country = country or ''
        self.city = city or ''
        self.street = street or ''

    def say_address(self):
        return f'Hero address: {self.country}, {self.city}, {self.street}'


class Weapon:
    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand or 'Sword'
        self.right_hand = right_hand or 'Bow'


#class Hero(Person, Address, Weapon):
class Hero(Person):

    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)

    def level_up(self, num: int):
        if self._check_level():
            self.level += 1
        else:
            self.level = self._max_level

    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2

    def add_many_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up * 2)

# p1 = Hero('archery', 'Rich', 'new', 'm')
# print(p1.name, p1.power, p1.up)





