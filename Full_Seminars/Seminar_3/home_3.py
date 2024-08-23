'''
Дан список повторяющихся элементов lst.
Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
'''
lst = [1, 3, 3, 2, 5, 6]
dict_1 = {}
for el in lst:
    dict_1[el] = dict_1.get(el, 0) + 1
print([key for key, value in dict_1.items() if value > 1])

lst = [1, 1, 2, 2, 3, 3]
print(list({i for i in lst}))
