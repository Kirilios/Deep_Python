"""
Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""

import json
import csv


def creat_csv():
    with open('task8_2.json', "r", encoding='utf-8') as js_f:
        res = json.load(js_f)
        keys = res[0].keys()
        lst = []
        lst.append(keys)
        for line in res:
            values = line.values()
            lst.append(values)

    with open('task8_2.csv', "w", newline='', encoding='utf-8') as cs_f:
        writer = csv.writer(cs_f)
        writer.writerows(lst)

creat_csv()

