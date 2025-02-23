import random
import sqlite3

conn = sqlite3.connect("LES32.db")
cursor = conn.cursor()
#
# cursor.execute("DROP TABLE IF EXISTS orders;")
# cursor.execute("DROP TABLE IF EXISTS products;")
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS products(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     price REAL NOT NULL,
#     stock INTEGER NOT NULL
# );
# """)
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS orders(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     quantity INTEGER NOT NULL,
#     total_price REAL NOT NULL,
#     order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     product_id INTEGER NOT NULL,
#     FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
# );
# """)
#
# cursor.executemany('''INSERT INTO products (name, price, stock) VALUES (?,?,?)''',
#                    [('iphone 13', 500, 10),
#                     ('iphone 14', 600, 5),
#                     ('iphone 15', 700, 16),
#                     ('iphone 16', 800, 100)])

# model = random.randint(1, 4)
# cursor.execute(f'SELECT price FROM products WHERE id= {model}')
# product_price = cursor.fetchone()[0]
# quantity = random.randint(1, 11)
# total_price = product_price * quantity
#
# cursor.execute(f'''
# INSERT INTO orders (product_id, quantity, total_price) VALUES ({model}, {quantity}, {total_price})
# ''')
#
# cursor.execute('UPDATE products SET price = 550 WHERE id = 1')
# cursor.execute(f'UPDATE orders SET quantity = 3, total_price = 2100 WHERE id = 1')
#
# print('Products:')
# cursor.execute('SELECT * FROM products;')
# products = cursor.fetchall()
# for product in products:
#     print(product)
#
# cursor.execute('''SELECT orders.id, products.name, orders.quantity, orders.total_price, orders.order_date
#                FROM orders
#                JOIN products ON orders.product_id = products.id''')
#
# print('Orders:')
# # cursor.execute('SELECT * FROM orders;')
# orders = cursor.fetchall()
# for order in orders:
#     print(order)

# cursor.execute("SELECT * FROM products WHERE name LIKE '%5'")
# cursor.execute("SELECT * FROM products WHERE price > 650")
# cursor.execute("SELECT * FROM orders WHERE total_price > 2000 ORDER BY total_price ASC")
# cursor.execute("SELECT DISTINCT total_price FROM orders")
# cursor.execute("SELECT COUNT(*) AS total_orders FROM orders")
# cursor.execute("SELECT COUNT(DISTINCT product_id) AS unique_products FROM orders")
# cursor.execute("SELECT SUM(total_price) FROM orders")
# cursor.execute("SELECT SUM(quantity) FROM orders")
# cursor.execute("SELECT AVG(price) FROM products")
# cursor.execute("SELECT AVG(total_price) FROM orders")
# cursor.execute("SELECT MAX(price) FROM products")
# cursor.execute("SELECT MIN(price) FROM products")
# cursor.execute("SELECT product_id, SUM(total_price) AS total_sales FROM orders GROUP BY product_id")
# products = cursor.fetchall()
# for product in products:
#     print(product)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT UNIQUE NOT NULL
# );
# """)

# cursor.execute("""ALTER TABLE orders ADD COLUMN user_id INTEGER REFERENCES users(id) ON DELETE CASCADE""")

# cursor.execute("""INSERT INTO users (name, email) VALUES ('Ivan', 'ivan@gmail.com'),
# ('Ilon', 'ilon@gmail.com'), ('Boris', 'boris@gmail.com'), ('Oleg', 'oleg@gmail.com')""")

# cursor.execute("""SELECT orders.id, users.name AS user_name, products.name AS product_name, orders.quantity, orders.Total_price, orders.order_date
# FROM orders
# JOIN users ON orders.user_id = users.id
# JOIN products ON orders.product_id = products.id
# """)

# cursor.execute("""SELECT orders.id, users.name AS user_name, products.name AS product_name, orders.quantity, orders.Total_price, orders.order_date
# FROM orders
# JOIN users ON orders.user_id = users.id
# JOIN products ON orders.product_id = products.id
# WHERE user_name = 'Ivan'
# """)

# cursor.execute("""SELECT orders.id, users.name AS user_name, products.name AS product_name, orders.quantity, orders.Total_price, orders.order_date
# FROM orders
# JOIN users ON orders.user_id = users.id
# JOIN products ON orders.product_id = products.id
# ORDER BY orders.total_price DESC
# """)

cursor.execute("""SELECT users.name AS user_name, SUM(orders.Total_price) as total_spent
FROM orders
JOIN users ON orders.user_id = users.id
GROUP BY users.id
ORDER BY total_spent
""")

products = cursor.fetchall()
for product in products:
    print(product)

conn.commit()
conn.close()
