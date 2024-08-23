"""
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""


from os import (listdir,
                makedirs,
                path,
                remove,
                urandom)
from shutil import rmtree
from random import choice, randint, sample
from string import ascii_lowercase, digits
# from sem_7_task_4 import create_files


folder_path = 'C:/Users/D/PycharmProjects/gb_py_submerge/sem_7_files'


def create_files(extension,
                 min_len=6, max_len=30,
                 min_bytes=256, max_bytes=4096,
                 amount=42, dir_path=folder_path):
    if not path.exists(dir_path):
        makedirs(dir_path)
    for _ in range(amount):
        filename = (f'{choice(ascii_lowercase)}'
                    f'{''.join((sample(ascii_lowercase + digits, randint(min_len - 1, max_len - 1))))}'
                    f'.{extension}')
        if path.isfile(path.join(dir_path, filename)):
            continue
        else:
            with open(path.join(dir_path, filename), 'wb') as f:
                file_size = randint(min_bytes, max_bytes)
                f.write(urandom(file_size))


def gen_files(*args, files_amount=5):
    for _ in range(files_amount):
        extension = choice(args)
        create_files(extension, amount=1)


def clear_folder(dir_path):
    if path.exists(dir_path):
        for filename in listdir(dir_path):
            file_path = path.join(dir_path, filename)
            if path.isfile(file_path):
                remove(file_path)
            elif path.isdir(file_path):
                rmtree(file_path)
        print(f'Directory "{dir_path}" has been cleared.')
    else:
        print(f'Directory "{dir_path}" not found.')


if __name__ == '__main__':
    gen_files('txt', 'jpg', 'zip', 'rtf')