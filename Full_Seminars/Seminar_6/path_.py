'''
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

import os

file_path = "C:/Users/User/Documents/example.txt"
file_path2 ='file_in_current_directory.txt'
file_path3 = 'D:/myfile.txt'
def get_file_info(file_path: str):
    #dir_path = os.path.dirname(file_path) + os.altsep - меняет сепаратор на '/'
    norm_path = os.path.normpath(file_path).replace(os.path.sep, '/')
    dir_name = os.path.dirname(norm_path)
    if os.path.dirname(dir_name) == '':
        pass
    else:
        if not dir_name.endswith('/'):
            dir_name += '/'
    file_name_and_ext = os.path.basename(file_path)
    file_name, file_extension = os.path.splitext(file_name_and_ext)  # делит имя файла и расширение и кидает их в кортеж
    return dir_name, file_name, file_extension


print(get_file_info(file_path))

#2
def get_file_info(file_path: str):
    norm_path = os.path.normpath(file_path).replace(os.path.sep, '/')
    dir_name = os.path.dirname(norm_path)
    if dir_name and not dir_name.endswith('/'):
        dir_name += '/'

    if not dir_name and norm_path:
        dir_name = ''

    file_name_and_ext = os.path.basename(norm_path)
    file_name, file_extension = os.path.splitext(file_name_and_ext)

    return dir_name, file_name, file_extension

print(get_file_info(file_path3))