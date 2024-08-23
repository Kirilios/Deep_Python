import os
from pathlib import Path

#os.path.join(os.getcwd(), 'Seminar_1', 'home_1.py')
print(os.path.join(os.getcwd(), 'Seminar_1', 'home_1.py'))
f = (Path().cwd() / 'Seminar_1' / 'home_1.py')
print((Path().cwd() / 'Seminar_1' / 'home_1.py'))

with open('newfile.txt', 'w', encoding='utf-8') as file:
    file.write('privet')
    print(file)