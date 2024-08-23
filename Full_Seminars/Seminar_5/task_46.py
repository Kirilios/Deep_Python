"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""

def prime_generator(n):
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


print(*prime_generator(30))

# Вариант 2

# def prime_generator(n):
#     count = 0
#     num = 2
#     while count < n:
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield num
#             count += 1
#         num += 1


# print(*prime_generator(30))
# matrix
def transpose(matrix):
    transposed = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]
    return transposed

# Введите ваше решение ниже

#def transpose(matrix):
    #return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

#transposed_matrix = transpose(matrix)

# print(transposed_matrix)

#bank
import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

# Введите ваше решение ниже


def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    else:
        return False


def deposit(amount):
    global bank_account
    if check_multiplicity(amount):
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    else:
        print(f'Сумма должна быть кратной 50 у.е.')


def withdraw(amount):
    global bank_account
    if not check_multiplicity(amount):
        print(f'Сумма должна быть кратной 50 у.е.')
    withdrawal_fee = int(amount * PERCENT_REMOVAL)
    if withdrawal_fee < MIN_REMOVAL:
        withdrawal_fee = MIN_REMOVAL
    elif withdrawal_fee > MAX_REMOVAL:
        withdrawal_fee = MAX_REMOVAL

    withdrawal_amount = int(amount + withdrawal_fee)
    if bank_account >= withdrawal_amount:
        bank_account -= withdrawal_amount
        operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {withdrawal_fee} у.е.. Итого {bank_account} у.е.')
    else:
        operations.append(f'Недостаточно средств. Сумма с комиссией {withdrawal_amount} у.е. На карте {bank_account} у.е.')



def exit():
    global bank_account
    if bank_account > RICHNESS_SUM:
        wealth_tax = round(bank_account * RICHNESS_PERCENT, 4)
        bank_account -= wealth_tax
        operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {wealth_tax} у.е. Итого {bank_account} у.е.')

    operations.append(f'Возьмите карту на которой {bank_account} у.е.')



#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#deposit(1000)
#withdraw(200)
#exit()

#print(operations)

def check_multiplicity(amount):
    """Проверка кратности суммы"""
    if (amount % MULTIPLICITY) != 0:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False
    return True

def deposit(amount):
    """Пополнение счета"""
    global bank_account, count
    if not check_multiplicity(amount):
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
