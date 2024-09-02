'''
Задача 2. Объединение данных из нескольких JSON файлов
Напишите скрипт, который объединяет данные из нескольких JSON файлов в
один. Каждый файл содержит список словарей, описывающих сотрудников
компании (имя, фамилия, возраст, должность). Итоговый JSON файл должен
содержать объединённые списки сотрудников из всех файлов.
'''

import json
import glob

def merge_json(input_files, output_files):
    merged_data = []
    for file in input_files:
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                merged_data.extend(data)
        except json.JSONDecodeError:
            print(f'Ошибка декодирования JSON в файле: {file}')

    with open(output_files, 'w') as f:
        json.dump(merged_data, f, indent=4)

if __name__ == "__main__":
    input_files =glob.glob('employees*.json')
    merge_json(input_files, 'all_employees.json')
