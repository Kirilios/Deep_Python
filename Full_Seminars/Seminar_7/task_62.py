"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.

"""


from functools import reduce


def read_2_files(filename_1: str, filename_2: str):
    with (
        open(filename_1, 'r', encoding='utf-8') as f_numbers,
        open(filename_2, 'r', encoding='utf-8') as f_names,
    ):

        num_products = [reduce(lambda x, y: x * y, map(float, line.split('|')))
                        for line in f_numbers.readlines()]
        names = [name.strip('\n') for name in f_names.readlines()]
        delta = abs(len(names) - len(num_products))

        if delta:
            for i in range(delta):
                if len(names) > len(num_products):
                    num_products.append(num_products[i])
                else:
                    names.append(names[i])
def write_2_files(filename: str, func):
    with open(filename, 'w', encoding='utf-8') as f:
        for name, number in func:
            name = name.lower() if number < 0 else name.upper()
            number = -number if number < 0 else int(number)
            print(f'{name} {number}', file=f)


if __name__ == '__main__':
    print(*read_2_files('sem_7_task_1.txt', 'sem_7_task_2.txt'), sep='\n')
    print(write_2_files('sem_7_task_3.txt',
                        read_2_files('sem_7_task_1.txt',
                                     'sem_7_task_2.txt')))