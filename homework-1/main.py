"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

# connect to db
with psycopg2.connect(host='localhost',database='north',user='postgres',password='5432') as conn:
    with conn.cursor() as cur:

        with open("north_data\customers_data.csv") as customers_file, \
             open("north_data\employees_data.csv") as employees_file, \
             open("north_data\orders_data.csv") as orders_file:

            customers_data = csv.reader(customers_file)
            next(customers_data)
            employees_data = csv.reader(employees_file)
            next(employees_data)
            orders_data = csv.reader(orders_file)
            next(orders_data)

            for customers in customers_data:
                cur.execute("INSRT INTO customers VALUES (%s, %s, %s)", customers)

            for employee in employees_data:
                cur.execute("INSRT INTO employees VALUES (%s, %s, %s, %s, %s)", employee)

            for order in orders_data:
                cur.execute("INSRT INTO orders VALUES (%s, %s, %s, %s, %s)", order)

conn.close()

