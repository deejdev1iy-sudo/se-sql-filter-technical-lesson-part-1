import sqlite3
import pandas as pd # type: ignore

conn = sqlite3.connect('data.sqlite')

employees = pd.read_sql("""
SELECT *
  FROM employees;
""", conn)

print(employees)

employees_names = pd.read_sql("""
SELECT firstName, lastName, email
  FROM employees
 WHERE lastName = "Firrelli";
""", conn)
print(employees_names)

employees_initial = pd.read_sql("""
SELECT *, length(firstName) AS letter_length
  FROM employees
  WHERE letter_length = 4;
""", conn)
print(employees_initial)

employee_first_initial = pd.read_sql("""
SELECT *, substr(firstName, 1, 1) AS last_initial
  FROM employees
 WHERE Last_initial = "M";
""", conn)
print(employee_first_initial)

price_order = pd.read_sql("""
SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int
  FROM orderDetails
 WHERE rounded_price_int = 30;
""", conn)
print(price_order)

placed_order = pd.read_sql("""
SELECT *, strftime("%m", orderDate) AS month
  FROM orders
 WHERE month = "01";
""", conn)
print(placed_order)