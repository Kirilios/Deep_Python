'''
В большой текстовой строке text подсчитать количество
 встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами.
Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф)
считать двумя словами.
Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
Пример
На входе:
text = 'Hello world. Hello Python. Hello again.'
На выходе:
[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
'''
#text = 'This is a sample text without repeating words.'
#text = "Python 3.9 is the latest version of Python. It's awesome!"
text = 'Hello world. Hello Python. Hello again.'
punctuation = ".,!?;:\'39"

text = ''.join(char if char not in punctuation else ' ' for char in text).lower()
words = text.split()
my_dict = {}
for word in words:
    my_dict[word] = my_dict.get(word, 0) + 1
my_dict = sorted(my_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)

print(my_dict)

#[('words', 1), ('without', 1), ('this', 1), ('text', 1), ('sample', 1), ('repeating', 1), ('is', 1), ('a', 1)]







#[('python', 2), ('version', 1), ('the', 1), ('s', 1), ('of', 1), ('latest', 1), ('it', 1), ('is', 1), ('awesome', 1)]