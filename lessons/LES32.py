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
cursor.execute("SELECT DISTINCT total_price FROM orders")
products = cursor.fetchall()
for product in products:
    print(product)

conn.commit()
conn.close()
