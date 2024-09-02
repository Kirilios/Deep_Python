'''
Задача 4. Агрегирование данных из CSV файла
Напишите скрипт, который считывает данные из CSV файла, содержащего
информацию о продажах (название продукта, количество, цена за единицу), и
подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в
новом CSV файле.
Пример: Из файла sales.csv нужно создать файл total_sales.csv, где для каждого
продукта будет указана общая выручка.
'''

import csv


def get_new_csv_file(old_csv_file, new_csv_file):
    sales_totals = {}
    with open(old_csv_file, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            product = row['product']
            quantity = int(row['quantity'])
            price = float(row['price'])
            total_sales = quantity * price
            if product in sales_totals:
                sales_totals[product] += total_sales
            else:
                sales_totals[product] = total_sales
    with open(new_csv_file, 'w', newline='', encoding='utf-8') as new_file_csv:
        writer = csv.DictWriter(new_file_csv, fieldnames=['название продукта', 'общая выручка'])
        writer.writeheader()
        for product, total_sale in sales_totals.items():
            writer.writerow({'название продукта': product, 'общая выручка': total_sale})

if __name__ == '__main__':
    get_new_csv_file('sales.csv', 'total_sales.csv')