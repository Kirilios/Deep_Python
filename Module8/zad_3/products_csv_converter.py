'''
Задача 3. Агрегирование данных из CSV файла
Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV
файл. JSON файл содержит данные о продуктах (название, цена, количество на
складе). В CSV файле каждая строка должна соответствовать одному продукту.
'''

import json
import csv

def json_to_csv(json_f, csv_f):
    with open(json_f, 'r') as f:
        data = json.load(f)
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Invalid JSON format")
    with open(csv_f, 'w', newline='') as csv_f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

if __name__ == '__main__':
    json_to_csv('products.json', 'products.csv')