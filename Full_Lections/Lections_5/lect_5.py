'''
a = 4356
b = 345
print(f'{a = }\t{b = }')

c, d, e = {'один', 'ldf', 'red'}
print(f'{c = }, {d = }, {e = }')
'''

# data = {'один', 'ldf', 'red', 'flag', 'zero',}
# c, d, f, *e = data
# print(f'{c = }, {d = }, {f = }, {e = }')
'''
data = [2,3,4,5,6,7,8]
for item in data:
    print(item, end='\t')
print()

data1 = [2,3,4,5,6,7,8]
print(*data1, sep='\t')

data2 = [2, 34, 56, 78]
list_iter = iter(data2)
print(list_iter)
print(*list_iter)

gen = (chr(i) for i in range(97, 123))
print(gen)
for char in gen:
    print(char)

lst = [chr(i) for i in range(97, 123)]
print(lst)
for char in lst:
    print(char)
'''
fata = [3, 56, 8, 43, 76, 769, 9, 99]
res = [item for item in fata if item % 3 == 0]
print(f'{res = }')

dict = {i: chr(i) for i in range(97, 123)}
print(dict)
for num , char in dict.items():
    print(f'dict[{num}] = {char}')

def factorial(n):
    number = 1
    result = []
    for i in range(1, n+1):
        number *= i
        result.append(number)
    return result

for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')