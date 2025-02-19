import random
import sqlite3

# connection = sqlite3.connect('LES31-1.db')
# cursor = connection.cursor()
#
# cursor.execute('''
# CREATE TABLE books(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT NOT NULL,
#     author TEXT NOT NULL,
#     published_year INTEGER CHECK (published_year > 0),
#     genre TEXT DEFAULT 'Unknown',
#     added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# ''')
#
# connection.commit()
# connection.close()
# print('database created')

# connection = sqlite3.connect('LES31-2.db')
# cursor = connection.cursor()
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS products(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     price REAL NOT NULL,
#     stock INTEGER NOT NULL
# );
# ''')
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
# connection.commit()
# connection.close()


connection = sqlite3.connect('LES31-2.db')
cursor = connection.cursor()
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS vegs_fruits(
#     name TEXT NOT NULL,
#     type TEXT CHECK (type = 'vegetables' OR type = 'fruits'),
#     colour TEXT NOT NULL,
#     calories INTEGER NOT NULL,
#     description TEXT NOT NULL
# );
# ''')

# cursor.executemany(f'''INSERT INTO vegs_fruits (name, type, colour, calories, description) VALUES (?, ?, ?, ?, ?)''',
#                    [('apple', 'fruits', 'red', 100, 'red apple'),
#                     ('cherry', 'fruits', 'red', 200, 'red cherry'),
#                     ('orange', 'fruits', 'yellow', 150, 'yellow orange'),
#                     ('cucumber', 'vegetables', 'green', 400, 'green cucumber'),
#                     ('tomato', 'vegetables', 'red', 90, 'red tomato'),
#                     ('cabbage', 'vegetables', 'green', 3000, 'green cabbage')])
# Відображення всієї інформації з таблиці овочів та фруктів;
# Відображення усіх овочів;
# Відображення усіх фруктів;
# Відображення усіх назв овочів та фруктів;
# Відображення усіх кольорів. Кольори мають бути унікальними;
# Відображення фруктів певного кольору;
# Відображення овочів певного кольору.

cursor.execute('SELECT * FROM vegs_fruits')
v_f = cursor.fetchall()
print(*v_f)
cursor.execute("SELECT * FROM vegs_fruits WHERE type = 'vegetables'")
vegs = cursor.fetchall()
print(vegs)
cursor.execute("SELECT * FROM vegs_fruits WHERE type = 'fruits'")
fruits = cursor.fetchall()
print(fruits)
cursor.execute("SELECT name FROM vegs_fruits")
names = cursor.fetchall()
print(names)
cursor.execute("SELECT DISTINCT colour FROM vegs_fruits ")
colours = cursor.fetchall()
print(colours)
cursor.execute("SELECT * FROM vegs_fruits WHERE colour = 'red' AND type = 'fruits'")
colour_red = cursor.fetchall()
print(colour_red)
cursor.execute("SELECT * FROM vegs_fruits WHERE colour = 'red' AND type = 'vegetables'")
colour_vegs = cursor.fetchall()
print(colour_vegs)

connection.commit()
connection.close()
