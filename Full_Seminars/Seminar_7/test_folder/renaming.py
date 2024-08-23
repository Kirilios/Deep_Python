'''
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files.
 Она должна: a. принимать параметр желаемое конечное имя файлов desired_name.
 При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере num_digits.
c. принимать параметр расширение исходного файла source_ext .
Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла target_ext.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории.
'''
import os
from pathlib import Path


def rename_files2(desired_name, num_digits, source_ext, target_ext, name_range=None):
    #if not os.path.exists('test_folder'):
    #    raise FileNotFoundError(f"The folder '{'test_folder'}' does not exist.")

    file_list = os.listdir()
    file_list = sorted([file for file in file_list if file.endswith(source_ext)])
    new_format = f'{{:0{num_digits}d}}'
    for i, file_name in enumerate(file_list):
        #original_name_part = file_name[3:6]
        base_name = file_name[:-len(source_ext)]
        start, end = name_range
        if end > len(base_name):
            end = len(base_name)
        original_name_part = base_name[start:end]
        new_name = f'{original_name_part}{desired_name}{new_format.format(i + 1)}.{target_ext}'

        old_file = os.path.join(os.getcwd(), file_name)
        new_file = os.path.join(os.getcwd(), new_name)

        os.rename(old_file, new_file)

    # desired_name = os.rename('old_names', 'new_name') + os.path.join(os.basename(desired_name))
    # os.path.
    import os
#2
def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    folder = 'test_folder'
    files = sorted ([f for f in os.listdir(folder) if f.endswith('.' + source_ext)])

    for i, file_name in enumerate(files):
        name, ext = os.path.splitext(file_name)
        if name_range:
            original_part = name[name_range[0]-1:name_range[1]]
        else:
            original_part = ''

        new_name = f"{original_part}{desired_name}{str(i+1).zfill(num_digits)}.{target_ext}"
        os.rename(os.path.join(folder, file_name), os.path.join(folder, new_name))