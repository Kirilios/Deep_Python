"""
Задание №6
Погружение в Python | Коллекции
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""

text: list = sorted('Я помню чудное мгновение, передо мной'.split())
long = len(max(text, key=len))

for i, word in enumerate(text, 1):
    print(f'{i}. {word:>{long}}')





