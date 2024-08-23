# list_1 = list()
# list_2 = list((3.14, True, 'Hello'))
# list_3 = []
# list_4 = [3.14, True, 'Hell']
# # первый индекс элемента всегда 0
# print(list_4[0])
# print(list_4[1])
# print(list_4[-1]) # индексация справва налево
#
# n = 33
# a = 'World'
# list_4.extend(a)
# # list_4.extend(n) # TypeError: 'int' object is not iterable
# print(list_4)

# list_2.extend(list_4)
# print(list_2)
# egg = list_2.pop(0)
# print(list_2, egg)
#
test = [1,2,2,45,77,45,8,8,9]
# tmp = test.count(8)
# print(tmp)
# tp = test.index(2)
# tp = test.index(45, 0, 6)

# test.insert(1, 666)
# print(test)
# test.insert(-2, 666)
# print(test)
#
# test.remove(77)
print(test)
test.sort()
sort_list = sorted(test)
print(test, sort_list, sep='\n')
new_rev_test = sorted(test, reverse=True)
print(new_rev_test)
new_l = test[::-1]
print(test, sep='\n')

# возвращается количество элем len(x)
print(len(test))
print(test.extend('25'))

text = 'What a shame'
print(text[3])
print(text[:4:])