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

cursor.execute('''
CREATE TABLE IF NOT EXISTS vegs_fruits(
    name TEXT NOT NULL,
    type TEXT CHECK (type = 'vegetables' OR type = 'fruits'),
    colour TEXT NOT NULL,
    calories INTEGER NOT NULL,
    description TEXT NOT NULL
);
''')

connection.commit()
connection.close()
