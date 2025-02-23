import sqlite3

# Створіть тритабличну базу даних Sales. У цій базі даних мають бути таблиці: Sales (інформація про конкретні продажі),
# Salesmen (інформація про продавців), Customers (інформація про покупців).
# Напишіть наступні запити

connection = sqlite3.connect('DZ33.db')
cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS salesmen(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# salesman_name NVARCHAR(255) NOT NULL CHECK (salesman_name != ''),
# edrpou INTEGER NOT NULL UNIQUE,
# rating REAL NOT NULL CHECK (rating >= 0 AND rating <= 5)
# );
# ''')
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS customers(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# first_name NVARCHAR(255) NOT NULL CHECK (first_name != ''),
# last_name NVARCHAR(255) NOT NULL CHECK (last_name != ''),
# tel NVARCHAR(10) NOT NULL UNIQUE,
# is_prime_status INTEGER NOT NULL CHECK (is_prime_status = '0' or is_prime_status = '1') DEFAULT '1'
# );
# ''')
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS sales(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# salesman REFERENCES salesmen(id) ON DELETE CASCADE,
# customer REFERENCES customers(id) ON DELETE CASCADE,
# products TEXT NOT NULL,
# total_price REAL NOT NULL CHECK (total_price >= 0) DEFAULT '0'
# );
# ''')
#
# cursor.executemany('''INSERT INTO salesmen (salesman_name, edrpou, rating) VALUES (?, ?, ?)''',
# [('Peter Johnson', 12345678, 4.5),
# ('Anna Smith', 23456789, 4.8),
# ('Michael Brown', 34567890, 4.2),
# ('Olivia Davis', 45678901, 4.7),
# ('Alex Wilson', 56789012, 4.9)])
#
#
# cursor.executemany('''INSERT INTO customers (first_name, last_name, tel, is_prime_status) VALUES (?, ?, ?, ?)''',
# [('John', 'Miller', '0501234567', 1),
# ('Emma', 'Taylor', '0672345678', 1),
# ('David', 'Anderson', '0633456789', 0),
# ('Sophie', 'Thomas', '0994567890', 1),
# ('James', 'White', '0505678901', 1),
# ('Lily', 'Martin', '0676789012', 0),
# ('Robert', 'Garcia', '0637890123', 1),
# ('Emily', 'Clark', '0998901234', 1),
# ('William', 'Lewis', '0509012345', 0),
# ('Sarah', 'Walker', '0670123456', 1)])
#
# cursor.executemany('''INSERT INTO sales (salesman, customer, products, total_price) VALUES (?, ?, ?, ?)''',
# [(1, 1, 'Samsung Galaxy S23 Phone, Case', 25000.50),
# (2, 2, 'Lenovo IdeaPad 5 Laptop', 32000.00),
# (3, 3, 'AirPods Pro Earbuds', 8500.75),
# (4, 4, 'iPad Air Tablet', 22000.25),
# (5, 5, 'Apple Watch Smartwatch', 13500.00),
# (1, 6, 'JBL Charge 5 Speaker', 6500.30),
# (2, 7, 'Dell 27" Monitor', 9800.00),
# (3, 8, 'Logitech Keyboard', 2500.50),
# (4, 9, 'Razer DeathAdder Mouse', 1800.25),
# (5, 10, 'TP-Link Archer Router', 3200.75),
# (1, 2, 'Samsung 1TB SSD', 4500.00),
# (2, 3, 'RTX 3060 Graphics Card', 14500.50),
# (3, 4, 'HP LaserJet Printer', 7800.25),
# (4, 5, '2TB External HDD', 3000.00),
# (5, 6, 'GoPro Hero 11 Camera', 16500.75),
# (1, 7, 'LG 55" TV', 28500.00),
# (2, 8, 'Samsung Air Conditioner', 22000.50),
# (3, 9, 'Panasonic Microwave', 4500.25),
# (4, 10, 'Delonghi Coffee Machine', 9800.00),
# (5, 1, 'Philips Electric Kettle', 1500.75),
# (1, 3, 'Tefal Iron', 2200.50),
# (2, 4, 'Dyson Vacuum Cleaner', 18500.00),
# (3, 5, 'Bosch Blender', 3500.25),
# (4, 6, 'Redmond Multicooker', 4200.75),
# (5, 7, 'Philips Toaster', 1800.00),
# (1, 8, 'Dyson Hair Dryer', 12500.50),
# (2, 9, 'Braun Electric Shaver', 6500.25),
# (3, 10, 'Air Humidifier', 2800.00),
# (4, 1, 'Xiaomi Lamp', 1200.75),
# (5, 2, 'TP-Link Smart Plug', 900.50),
# (1, 3, 'PlayStation 5 Console', 22500.00),
# (2, 4, 'HyperX Headset', 3500.25),
# (3, 5, 'Logitech Webcam', 2200.75),
# (4, 6, 'Anker Charger', 800.00),
# (5, 7, 'Philips Hue Smart Bulb', 1500.50),
# (1, 8, 'Kindle E-reader', 5500.25),
# (2, 9, 'Xiaomi Fitness Tracker', 1200.00),
# (3, 10, 'Xiaomi Smart Scale', 1800.75),
# (4, 1, 'Air Purifier', 6500.50),
# (5, 2, 'Robot Vacuum Cleaner', 14500.00),
# (1, 3, 'Epson Projector', 28500.25),
# (2, 4, 'Facial Sauna', 2500.75),
# (3, 5, 'Xiaomi Electric Scooter', 18500.00),
# (4, 6, 'DJI Mini Drone', 16500.50),
# (5, 7, 'Zhiyun Stabilizer', 7500.25),
# (1, 8, 'Smart TV Box', 3200.00),
# (2, 9, 'Xbox Controller', 2500.75),
# (3, 10, 'Razer Microphone', 3500.50),
# (4, 1, 'Office Chair', 8500.00),
# (5, 2, 'Canon Scanner', 4500.25)])

print('\nВідображення усіх угод')
cursor.execute("""
SELECT * 
FROM sales 
JOIN salesmen ON salesmen.id = sales.salesman 
JOIN customers ON customers.id = sales.customer
""")
sales = cursor.fetchall()
for sale in sales:
    print(f'Sale id: {sale[0]}; Salesman: {sale[6]} {sale[7]}; Customer: {sale[10]} {sale[11]} {sale[12]}; '
          f'Products: {sale[3]}; Total cost: {sale[4]}')

print('\nВідображення угод конкретного продавця')
cursor.execute("""
SELECT sales.id, sales.products, sales.total_price 
FROM sales 
JOIN salesmen ON salesmen.id = sales.salesman 
WHERE salesmen.salesman_name = 'Anna Smith'
""")
sales = cursor.fetchall()
for sale in sales:
    print(sale)

print('\nВідображення максимальної за сумою угоди')
cursor.execute("""
SELECT *, MAX(total_price)
FROM sales 
JOIN salesmen ON salesmen.id = sales.salesman 
JOIN customers ON customers.id = sales.customer
""")
sales = cursor.fetchall()
for sale in sales:
    print(sale[:-1])

print('\nВідображення мінімальної за сумою угоди')
cursor.execute("""
SELECT *, MIN(total_price)
FROM sales 
JOIN salesmen ON salesmen.id = sales.salesman 
JOIN customers ON customers.id = sales.customer
""")
sales = cursor.fetchall()
for sale in sales:
    print(sale[:-1])

print('\nВідображення максимальної суми угоди для конкретного продавця')
cursor.execute("""
SELECT *, MAX(total_price)
FROM sales 
JOIN salesmen ON salesmen.id = sales.salesman 
JOIN customers ON customers.id = sales.customer 
WHERE salesmen.salesman_name = 'Olivia Davis'
""")
sales = cursor.fetchall()
for sale in sales:
    print(sale[:-1])

print('\nВідображення мінімальної за сумою угоди для конкретного продавця')
cursor.execute("""
SELECT *, MIN(total_price)
FROM sales 
JOIN salesmen ON salesmen.id = sales.salesman 
JOIN customers ON customers.id = sales.customer 
WHERE salesmen.salesman_name = 'Alex Wilson'
""")
sales = cursor.fetchall()
for sale in sales:
    print(sale[:-1])

print('\nВідображення максимальної за сумою угоди для конкретного покупця')
cursor.execute("""
SELECT *, MAX(total_price)
FROM sales 
JOIN salesmen ON salesmen.id = sales.salesman 
JOIN customers ON customers.id = sales.customer 
WHERE customers.last_name = 'Thomas'
""")
sales = cursor.fetchall()
for sale in sales:
    print(sale[:-1])

print('\nВідображення мінімальної за сумою угоди для конкретного покупця')
cursor.execute("""
SELECT *, MIN(total_price)
FROM sales 
JOIN salesmen ON salesmen.id = sales.salesman 
JOIN customers ON customers.id = sales.customer 
WHERE customers.last_name = 'White'
""")
sales = cursor.fetchall()
for sale in sales:
    print(sale[:-1])

print('\nВідображення продавця з максимальною сумою продажів за всіма угодами')
cursor.execute("""
SELECT salesmen.salesman_name, salesmen.edrpou, salesmen.rating, SUM(sales.total_price) AS total_sales
FROM sales 
JOIN salesmen ON salesmen.id = sales.salesman
GROUP BY salesmen.id, salesmen.salesman_name, salesmen.edrpou, salesmen.rating
HAVING SUM(sales.total_price) = (
    SELECT SUM(sales.total_price)
    FROM sales
    GROUP BY sales.salesman
    ORDER BY SUM(sales.total_price) DESC
    LIMIT 1
)
""")
sales = cursor.fetchall()
print(*sales)

print('\nВідображення продавця з мінімальною сумою продажів за всіма угодами')
cursor.execute("""
SELECT salesmen.salesman_name, salesmen.edrpou, salesmen.rating, SUM(sales.total_price) AS total_sales
FROM sales 
JOIN salesmen ON salesmen.id = sales.salesman
GROUP BY salesmen.id, salesmen.salesman_name, salesmen.edrpou, salesmen.rating
HAVING SUM(sales.total_price) = (
    SELECT SUM(sales.total_price)
    FROM sales
    GROUP BY sales.salesman
    ORDER BY SUM(sales.total_price) ASC
    LIMIT 1
)
""")
sales = cursor.fetchall()
print(*sales)

print('\nВідображення покупця з максимальною сумою покупок за всіма угодами')
cursor.execute("""
SELECT customers.first_name, customers.last_name, customers.tel, 
customers.is_prime_status, SUM(sales.total_price) AS total_sales 
FROM sales 
JOIN customers ON customers.id = sales.customer
GROUP BY customers.first_name, customers.last_name, customers.tel, customers.is_prime_status
HAVING SUM(sales.total_price) = (
    SELECT SUM(sales.total_price)
    FROM sales
    GROUP BY sales.customer
    ORDER BY SUM(sales.total_price) DESC
    LIMIT 1
)
""")
sales = cursor.fetchall()
print(*sales)

print('\nВідображення середньої суми покупки для конкретного покупця')
cursor.execute("""
SELECT customers.first_name, customers.last_name, customers.tel, 
customers.is_prime_status, AVG(sales.total_price) AS avg_sales 
FROM sales 
JOIN customers ON customers.id = sales.customer
WHERE customers.last_name = 'Anderson'
GROUP BY customers.first_name, customers.last_name, customers.tel, customers.is_prime_status 
""")
sales = cursor.fetchall()
print(*sales)

print('\nВідображення середньої суми покупки для конкретного продавця')
cursor.execute("""
SELECT salesmen.salesman_name, salesmen.edrpou, salesmen.rating, SUM(sales.total_price) AS total_sales
FROM sales 
JOIN salesmen ON salesmen.id = sales.salesman
WHERE salesmen.salesman_name = 'Peter Johnson'
GROUP BY salesmen.id, salesmen.salesman_name, salesmen.edrpou, salesmen.rating
""")
sales = cursor.fetchall()
print(*sales)

connection.commit()
connection.close()


