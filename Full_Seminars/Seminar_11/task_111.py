"""
Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""
import time

class MyString(str):

    def __new__(cls, author, string, creation_time=None):
        if creation_time is None:
            creation_time = time.time()
        obj = super().__new__(cls, string)
        obj.author = author
        obj.creation_time = creation_time
        return obj

    def __str__(self):
        return f"{super().__str__()} (автор: {self.author}, создано: {time.ctime(self.creation_time)})"

    def __repr__(self):
        return f"MyString({self.author}, {time.ctime(self.creation_time)})"

if __name__ == '__main__':
    pass

