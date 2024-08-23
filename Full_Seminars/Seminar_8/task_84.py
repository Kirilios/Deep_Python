"""
Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""

import csv
import json


with open('task8_2.csv', encoding="utf-8") as f:
    fr = csv.reader(f)
    res = list(fr)
    print(res)
    for i in range(1,len(res)):
        cur_id = res[i][1]
        res[i][1] = f"{cur_id.zfill(10)}"
        res[i][2] = res[i][2].title()
        res[i].append(hash(res[i][2]))
    res[0].append('hash')

with open('new_json.json', "w", encoding="utf-8") as j:
    json.dump(res, j, ensure_ascii=False)