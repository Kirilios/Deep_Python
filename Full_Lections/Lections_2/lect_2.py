import math
import decimal
import fractions

'''
f = 5
l = 28.7
print(type(f))
print(id(l))
print(isinstance(f,float))
a = 'Hello'
print(type(a), id(a))
# логические  типы True/False являются подклассом int
g = True
print(isinstance(g,int))
m = 436.5687
print(isinstance(m,(int, float, complex)))

num = 2 + 2 * 2
digit = 36/6
print(num,digit)
print(num == digit)
print(num is digit)

print(f, id(f))
f += 1
print(f, id(f))

text = 'Hi friend'
print(text, id(text))
text = text.replace(' ', '_')
print(text, id(text))
print(hash(text))

txt = input('Enter your text: ')
if isinstance(txt, (int, float, str, bool, complex, tuple, set, bytes)):
    print(f' Тип = {type(txt)}''\n'
          f' ID = {id(txt)}''\n'
          f' Hash = {hash(txt)}')
elif txt == None:
    print('Вы ничего не ввели')
else:
    print('Ваш тип изменяемый, введите другой текст')
'''
# b: float | int = 234.54
# a: float = 32.4
# b = b/a
# print(b)
#
# import typing
#
# print("Hello".__doc__)
# print("what is it".upper())
# print("what is it".capitalize())
# print("what is it".count('t'))
# print(dir())
# print(help())
# a = int(34.555)
# b = int('253')
# c = int('Good', base=36)
# print(a, b, c, sep='\n')

# num = 2 ** 16 - 1
# b = bin(num)
# o = oct(num)
# h = hex(num)
# print(b, o, h)
# f = 3255634
# print(str(f))
'''
LIMIT = 120
ATTENTION = 'Attention!'
name = input('What is your name? ')
age = int(input('How old are you? '))

text = ATTENTION + ' Even though you have got ' + \
       str(100 - age) + " until you reach 100 years, but the length" \
                        " of string mustn't exceed " + \
       str(LIMIT) + ' symbols.'
print(text)
'''
# ATTENTION = 'Attention!'
# f = 'Ваш тип изменяемый, введите другой текст'
# print(ATTENTION.__sizeof__())
# print(f.__sizeof__())
#
# txt = input("Enter your text: ")
# try:
#     num = int(txt)
#     print(bin(num), oct(num), hex(num))
# except ValueError:
#     # if not txt.isascii():
#     #     print('Not in ASCII')
#     # else:
#     #     print('written in ASCII')
#     print('Not in ASCII' if not txt.isascii() else 'written in ASCII')
# # finally:
# #     quit()

print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')
print(dir(math))
print(help(math.gcd))