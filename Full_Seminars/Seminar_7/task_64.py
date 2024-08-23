"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.

"""

from os import listdir, path, remove
from shutil import rmtree
from random import choice
from task_63 import create_files


folder_path = 'C:/Users/D/PycharmProjects/gb_py_submerge/sem_7_files'


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
        print(f"Directory '{dir_path}' has been cleared.")
    else:
        print(f"Directory '{dir_path}' not found.")


if __name__ == '__main__':
    if listdir(folder_path):
        clear_folder(folder_path)
    else:
        gen_files('txt', 'jpg', 'zip', 'rtf')