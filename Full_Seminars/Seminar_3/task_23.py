"""
Задание №4
Погружение в Python | Коллекции
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""

my_list = [1, 3, 5, 2, 6, 7, 43, 8, 9, 4, 3, 5, 6, 1, 56]

count = {}
for item in my_list:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

# Исправляем создание списка unique_list
unique_list = [item for item in my_list if count[item] == 1]

# Выводим результат
print(unique_list)

# 2

my_list = [1, 5, 3, 5, 2, 2, 5]

count_dict = {}
for item in my_list:
    count_dict[item] = count_dict.get(item, 0) + 1

my_list_copy = my_list[:]

for i in range(len(my_list_copy)):
    if count_dict[my_list_copy[i]] == 2:
        my_list.remove(my_list_copy[i])

print(my_list)