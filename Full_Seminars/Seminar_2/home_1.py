'''
Напишите программу, которая получает целое число num и
возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

num = 0
ZERO = 0
if num is ZERO:
    print('Шестнадцатеричное представление числа: ' + '')
    print('Проверка результата: ' + hex(num))
else:
    num = "{:02x}".format(num).upper()
    print('Шестнадцатеричное представление числа: ' + num)
    hex_identifier = '0x'
    new_str = hex_identifier + num.lower()
    print('Проверка результата: ' + new_str)

# print(f'Проверка результата: {hex(num)}')
# print(help(str))

# option 2
HEX = 16
hex_digits = "0123456789ABCDEF"

hex_num = ""
test_hex_num = hex(num)

while num > 0:
    remainder = num % HEX
    hex_num = hex_digits[remainder] + hex_num
    num //= HEX

print("Шестнадцатеричное представление числа:", hex_num)
print("Проверка результата:", test_hex_num)