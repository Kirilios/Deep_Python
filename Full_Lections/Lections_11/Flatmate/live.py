'''
Задача 2. Совместное проживание
Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом
одиночестве, Артём решил провести необычное исследование. Для этого он
реализовал модель человека и модель дома.
Человек может (должны быть такие методы):
● есть (+ сытость, − еда);
● работать (− сытость, + деньги);
● играть (− сытость);
● ходить в магазин за едой (+ еда, − деньги);
● прожить один день (выбирает одно действие согласно описанному ниже
приоритету и выполняет его).
У человека есть (должны быть такие атрибуты):
● имя,
● степень сытости (изначально 50),
● дом.
В доме есть:
● холодильник с едой (изначально 50 еды),
● тумбочка с деньгами (изначально 0 денег).
Если сытость человека становится меньше нуля, человек умирает.
Логика действий человека определяется следующим образом:
1. Генерируется число кубика от 1 до 6.
2. Если сытость < 20, то нужно поесть.
3. Иначе, если еды в доме < 10, то сходить в магазин.
4. Иначе, если денег в доме < 50, то работать.
5. Иначе, если кубик равен 1, то работать.
6. Иначе, если кубик равен 2, то поесть.
7. Иначе играть.
По такой логике эксперимента человеку надо прожить 365 дней.
Реализуйте такую программу и создайте двух людей, живущих в одном доме.
Проверьте работу программы несколько раз.
'''

import random

class House:
    """Класс House в котором живет класс Human. Имеет дандер метод __init__() и методы:
    buy_food, earn_money."""

    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money

    def buy_food(self, amount, price):
        if self.money >= price:
            self.food += amount
            self.money -= price
            print(f'Bought {amount = } food for {price = } money')
        else:
            print('Not enough money')

    def earn_money(self, salary):
        self.money += salary
        print(f'Earned {salary = } money')

class Human:
    """Класс Human симулирующий поведение человека. Проживает в классе House
    Имеет методы: """

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 50

    def eat(self):
        if self.house.food >= 10:
            self.fullness += 10
            self.house.food -= 10
            print(f'{self.name} ate 10 food. '
                f'Fullness has increased {self.fullness}, ',
                f'food has decreased {self.house.food}.')
        else:
            print(f'{self.name} is hungry, because there is no food in the house')

    def work(self):
        self.fullness -= 10
        self.house.earn_money(50)
        print(f'{self.name} worked. '
                f'Fullness has decreased {self.fullness}, ',
                f'money has increased {self.house.money}.')

    def play(self):
        self.fullness -= 5
        print(f'{self.name} played. '
                f'Fullness has decreased {self.fullness}.')

    def shop_for_food(self):
        self.house.buy_food(15, 20)

    def live_day(self):
        """for modelling of a single day of life of human"""
        dice_roll = random.randint(1, 6)
        print(f'Throwing dice {dice_roll}')
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shop_for_food()
        elif self.house.money < 50:
            self.work()
        elif dice_roll == 1:
            self.work()
        elif dice_roll == 2:
            self.eat()
        else:
            self.play()

        if self.fullness <= 0:
            print(f'{self.name} died. Fullness: {self.fullness}')
            return False
        return True


if __name__ == '__main__':
    house1 = House()
    human1 = Human('Arthur', house1)
    human2 = Human('Mary', house1)

    house2 = House()
    human3 = Human('John', house2)

    try:
        for day in range(1, 366):
            print(f'\nDay: {day}')
            human1_alive = human1.live_day()
            human2_alive = human2.live_day()
            human3_alive = human3.live_day()

            if not human1_alive or not human2_alive or not human3_alive:
                print(f'\033х91m*** Human has died on day: {day} ***\033[0m')
                break

    finally:

        print('End of simulation')

        print('State of a couple:')
        print(f'food in fridge - {house1.food}, money - {house1.money}')
        print(f'State of {human1.name}: fullness - {human1.fullness}')
        print(f'State of {human2.name}: fullness - {human2.fullness}')

        print('bachelors state:')
        print(f'food in fridge - {house2.food}, money - {house2.money}')
        print(f'State of {human3.name}: fullness - {human3.fullness}')