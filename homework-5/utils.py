import json

import psycopg2
from typing import List


def create_database(db_name: str, params: dict) -> None:
    """Создаёт новую базу данных."""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
    cur.execute(f'CREATE DATABASE {db_name}')

    cur.close()
    conn.close()


def execute_sql_script(cur, script_file) -> None:
    """Выполняет скрипт из файла для заполнения БД данными."""
    with open(script_file, 'r', encoding="UTf-8") as f:
        sql = f.read()

    cur.execute(sql)


def create_suppliers_table(cur) -> None:
    """Создает таблицу suppliers."""
    cur.execute("""
        CREATE TABLE suppliers (
            supplier_id serial PRIMARY KEY,
            company_name varchar,
            contact varchar,
            address varchar,
            phone varchar,
            fax varchar,
            homepage varchar,
            products text
        )
    """)


def get_suppliers_data(json_file: str) -> List[dict]:
    """Извлекает данные о поставщиках из JSON-файла и возвращает список словарей с соответствующей информацией."""
    with open(json_file, 'r', encoding="UTf-8") as f:
        data = json.load(f)

    return data


def insert_suppliers_data(cur, suppliers: List[dict]) -> None:
    """Добавляет данные из suppliers в таблицу suppliers."""
    for i in suppliers:
        cur.execute(
            """
            INSERT INTO suppliers (company_name, contact, address, phone, fax, homepage, products)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING supplier_id
            """,
            (i['company_name'], i['contact'], i['address'], i['phone'], i['fax'], i['homepage'], i['products'])
        )


def add_foreign_keys(cur, json_file) -> None:
    """Добавляет foreign key со ссылкой на supplier_id в таблицу products."""
    with open(json_file, 'r') as file:   # Чтение JSON файла
        json_data = json.load(file)
    cur.execute("""ALTER TABLE products ADD COLUMN supplier_id int""")

    for index, supplier in enumerate(json_data):
        supplier_id = index + 1  # Порядковый номер поставщика в JSON файле
        products = supplier['products']
        for product_name in products:
            escaped_product_name = product_name.replace("'", "''")  # Экранирование апострофов
            cur.execute(
                f"UPDATE products SET supplier_id = {supplier_id} WHERE product_name = '{escaped_product_name}';")

    # Добавление внешнего ключа
    cur.execute(
        "ALTER TABLE products ADD CONSTRAINT fk_supplier FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);")
