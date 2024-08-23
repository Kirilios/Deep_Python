'''
def open_file(file):
    p = open('file1.txt', mode='r')
    p.read()
    p.write("full opener")
    p.flush()
    p.close()

test = open_file('file1.txt')
'''
#test2 = open('file1.txt', encoding='utf-8')
#print(test2)
#print(list(test2))

import os

from pathlib import Path

#print(os.getcwd())

#print(Path.cwd())

# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(obj)

dir_list = os.listdir()

for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')

# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(f'{obj.is_dir() = }', end='\t')
#     print(f'{obj.is_file() = }', end='\t')
#     print(f'{obj.is_symlink() = }', end='\t')
#     print(f'{obj = }')
#print(Path(Path().cwd()))
# for dir_path, dir_name, file_name in os.walk(os.getcwd()):
#     print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')

#os.rename('file1.txt', 'file123.txt')

#Path('file123.txt').rename('file456.txt')