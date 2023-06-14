"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

'''Подставьте свой пароль'''
PASSWORD = '28101984'

'''Пути к csv файлам'''
employees_csv = 'north_data/employees_data.csv'
customers_csv = 'north_data/customers_data.csv'
orders_csv = 'north_data/orders_data.csv'

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password=PASSWORD)

try:
    with conn:
        with conn.cursor() as cur:
            '''Заполнение таблицы employees'''
            '''Открытие csv файла'''
            with open(employees_csv, 'r', encoding='utf8', newline='') as csv_file:
                data_file = csv.reader(csv_file, delimiter=',')
                skip_header = True  # для пропуска заголовков
                for data in data_file:
                    if skip_header:
                        skip_header = False
                        continue  # пропуск заголовков (1 строка)

                    '''Запрос на добавление данных в таблицу employees'''
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                (data[0], data[1], data[2], data[3], data[4], data[5]))

                    '''Запрос на чтение таблицы employees'''
                    cur.execute('SELECT * FROM employees')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)

            '''Заполнение таблицы customers'''
            '''Открытие csv файла'''
            with open(customers_csv, 'r', encoding='utf8', newline='') as csv_file:
                data_file = csv.reader(csv_file, delimiter=',')
                skip_header = True  # для пропуска заголовков
                for data in data_file:
                    if skip_header:
                        skip_header = False
                        continue  # пропуск заголовков (1 строка)

                    '''Запрос на добавление данных в таблицу customers'''
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                                (data[0], data[1], data[2]))

                    '''Запрос на чтение таблицы customers'''
                    cur.execute('SELECT * FROM customers')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)

            '''Заполнение таблицы orders'''
            '''Открытие csv файла'''
            with open(orders_csv, 'r', encoding='utf8', newline='') as csv_file:
                data_file = csv.reader(csv_file, delimiter=',')
                skip_header = True  # для пропуска заголовков
                for data in data_file:
                    if skip_header:
                        skip_header = False
                        continue  # пропуск заголовков (1 строка)

                    '''Запрос на добавление данных в таблицу orders'''
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                (data[0], data[1], data[2], data[3], data[4]))

                    '''Запрос на чтение таблицы orders'''
                    cur.execute('SELECT * FROM orders')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)

finally:
    conn.close()
