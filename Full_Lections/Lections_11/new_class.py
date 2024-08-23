import sys

class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Created {self.name = }')

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f'Created class {cls}')
        return instance

    # def __del__(self):
    #     print(f'deleted obj {self.name}')

    # def __str__(self):
    #     return f'Экземпляр класса User с именем "{self.name}"'

    def __repr__(self):
        return f'User({self.name})'

print('first class')
u_1 = User('Name')
print(sys.getrefcount(u_1))
print('sec class')
u_2 = User('Name2')
print(sys.getrefcount(u_2))
del u_2
print(sys.getrefcount(u_1))
print('third class')
u_3 = User('Name3')
print(u_3)

class NamedInt(int):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        print(f'new class {cls}')
        return instance

a = NamedInt(33, 'script')
print(f'{a = }\t{a.name = }, {type(a) = }')
b = NamedInt(66, 'new line')
print(f'{b = }\t{b.name = }, {type(b) = }')
c = a + b
print(f'{c = }\t{type(c) = }')

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str):
        self.name = name

a = Singleton('first')
print(f'{a.name = }')
b = Singleton('second')
print(f'{a is b =}')
print(f'{a.name = }\n{b.name = }')