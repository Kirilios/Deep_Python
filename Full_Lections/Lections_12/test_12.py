class Number:
    def __init__(self, num):
        self.num = num

n = Number(42)
print(callable(Number))
print(callable(n))

from collections import defaultdict

class Storage:
    def __init__(self):
        self.storage = defaultdict(list)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return f'Objects of storage of type:\n{txt}'

    def __call__(self, value):
        self.storage[type(value)].append(value)
        return f' to type {type(value)} added {value}'

s = Storage()
print(s(42))
print(s('Hello'))
print(s(0))
print(s)