import sqlite3

# Завдання 1
# Створіть наступні запити для таблиці з оцінками студентів:
#
# Відображати всієї інформації з таблиці зі студентами та оцінками.
# Відображати ПІБ усіх студентів.
# Відображати усіх середніх оцінок.
# Показати ПІБ усіх студентів з мінімальною оцінкою, більшою, ніж зазначена.
# Показати країни студентів. Назви країн мають бути унікальними.
# Показати міста студентів. Назви міст мають бути унікальними.
# Показати назви груп. Назви груп мають бути унікальними.
# Показати назви усіх предметів із мінімальними середніми оцінками. Назви предметів мають бути унікальними.
# Показати ПІБ усіх студентів з мінімальною оцінкою у вказаному діапазоні.
# Показати інформацію про студентів, яким виповнилося 20 років.
# Показати інформацію про студентів з віком, у вказаному діапазоні.
# Показати інформацію про студентів із конкретним ім'ям. Наприклад, показати студентів з ім'ям Борис.
# Показати інформацію про студентів, в номері яких є три сімки.
# Показати електронні адреси студентів, що починаються з конкретної літери.

connection = sqlite3.connect('DZ32.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students_marks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
city TEXT NOT NULL,
country TEXT NOT NULL,
bday_year INTEGER NOT NULL,
email TEXT,
tel INTEGER NOT NULL,
group_name TEXT NOT NULL,
avg_mark REAL NOT NULL,
subject_min_avg_mark TEXT NOT NULL,
subject_max_avg_mark TEXT NOT NULL
);
''')

# Данные для таблицы создал в ЧатГПТ =)
# cursor.executemany(f'''INSERT INTO students_marks (first_name, last_name, city, country, bday_year, email,
# tel, group_name, avg_mark, subject_min_avg_mark, subject_max_avg_mark) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
# [("John", "Smith", "New York", "USA", 2002, "john.smith@example.com", "+12125551234", "A1", 4.5, "Mathematics", "Computer Science"),
# ("Emily", "Johnson", "Los Angeles", "USA", 2001, "emily.johnson@example.com", "+13105557890", "B2", 4.2, "Physics", "Literature"),
# ("Michael", "Brown", "Toronto", "Canada", 2003, "michael.brown@example.com", "+14165552345", "C3", 4.8, "Chemistry", "Biology"),
# ("Sophia", "Williams", "Vancouver", "Canada", 2002, "sophia.williams@example.com", "+16045556789", "D4", 3.9, "History", "Geography"),
# ("Daniel", "Miller", "Chicago", "USA", 2001, "daniel.miller@example.com", "+17735551234", "A2", 4.6, "Social Studies", "Physics"),
# ("Olivia", "Davis", "London", "UK", 2003, "olivia.davis@example.com", "+442071234567", "B3", 4.3, "English", "French"),
# ("James", "Wilson", "Manchester", "UK", 2002, "james.wilson@example.com", "+441612345678", "C1", 3.7, "Literature", "Chemistry"),
# ("Charlotte", "Moore", "Edinburgh", "UK", 2001, "charlotte.moore@example.com", "+441315678901", "D2", 4.9, "Geography", "Mathematics"),
# ("Benjamin", "Taylor", "San Francisco", "USA", 2003, "benjamin.taylor@example.com", "+14155552345", "A3", 4.4, "Computer Science", "Physics"),
# ("Emma", "Anderson", "Montreal", "Canada", 2002, "emma.anderson@example.com", "+15145553456", "B1", 4.1, "French", "History"),
# ])

print('\nВідображати всієї інформації з таблиці зі студентами та оцінками.')
cursor.execute('SELECT * FROM students_marks')
all_info = cursor.fetchall()
for x in all_info:
    print(*x)

print('\nВідображати ПІБ усіх студентів.')
cursor.execute('SELECT first_name, last_name FROM students_marks')
all_names = cursor.fetchall()
for x in all_names:
    print(*x)

print('\nВідображати усіх середніх оцінок.')
cursor.execute('SELECT avg_mark FROM students_marks')
all_marks = cursor.fetchall()
for x in all_marks:
    print(x[0])

print('\nПоказати ПІБ усіх студентів з мінімальною оцінкою, більшою, ніж зазначена. 4.2')
cursor.execute('SELECT first_name, last_name FROM students_marks WHERE avg_mark >= 4.2')
all_marks_more_than = cursor.fetchall()
for x in all_marks_more_than:
    print(*x)

print('\nПоказати країни студентів. Назви країн мають бути унікальними.')
cursor.execute('SELECT DISTINCT country FROM students_marks')
distinct_country = cursor.fetchall()
for x in distinct_country:
    print(*x)

print('\nПоказати міста студентів. Назви міст мають бути унікальними.')
cursor.execute('SELECT DISTINCT city FROM students_marks')
distinct_city = cursor.fetchall()
for x in distinct_city:
    print(*x)

print('\nПоказати назви груп. Назви груп мають бути унікальними.')
cursor.execute('SELECT DISTINCT group_name FROM students_marks')
distinct_group_name = cursor.fetchall()
for x in distinct_group_name:
    print(*x)

print('\nПоказати назви усіх предметів із мінімальними середніми оцінками. Назви предметів мають бути унікальними.')
cursor.execute('SELECT DISTINCT subject_min_avg_mark FROM students_marks')
distinct_subject_min_avg_mark = cursor.fetchall()
for x in distinct_subject_min_avg_mark:
    print(*x)

print('\nПоказати ПІБ усіх студентів з мінімальною оцінкою у вказаному діапазоні. 4.0 - 4.4')
cursor.execute('SELECT first_name, last_name FROM students_marks WHERE avg_mark BETWEEN 4.0 AND 4.4')
all_marks_in_range = cursor.fetchall()
for x in all_marks_in_range:
    print(*x)

print('\nПоказати інформацію про студентів, яким виповнилося 23 роки.')
cursor.execute('SELECT first_name, last_name FROM students_marks WHERE bday_year <= 2002')
students_more_23_years_old = cursor.fetchall()
for x in students_more_23_years_old:
    print(*x)

print('\nПоказати інформацію про студентів з віком, у вказаному діапазоні. 22-23 роки.')
cursor.execute('SELECT first_name, last_name FROM students_marks WHERE bday_year BETWEEN 2002 AND 2003')
students_22_23_years_old = cursor.fetchall()
for x in students_22_23_years_old:
    print(*x)

print('\nПоказати інформацію про студентів із конкретним і\'мям. Наприклад, показати студентів з і\'мям John.')
cursor.execute('SELECT * FROM students_marks WHERE first_name = "John"')
students_name_John = cursor.fetchall()
for x in students_name_John:
    print(*x)

print('\nПоказати інформацію про студентів, в номері яких є три п\'ятірки.')
cursor.execute('SELECT * FROM students_marks WHERE tel LIKE "%555%"')
students_tel_555 = cursor.fetchall()
for x in students_tel_555:
    print(*x)

print('\nПоказати електронні адреси студентів, що починаються з конкретної літери.')
cursor.execute('SELECT * FROM students_marks WHERE email LIKE "e%"')
students_emael_starts_e = cursor.fetchall()
for x in students_emael_starts_e:
    print(*x)

connection.commit()
connection.close()

# Відображення усіх овочів з калорійністю, менше вказаної.
# Відображення усіх фруктів з калорійністю у вказаному діапазоні.
# Відображення усіх овочів, у назві яких є вказане слово. Наприклад, слово: капуста.
# Відображення усіх овочів та фруктів, у короткому описі яких є вказане слово. Наприклад, слово: гемоглобін.
# Показати усі овочі та фрукти жовтого або червоного кольору.

connection2 = sqlite3.connect('DZ32.db')
cursor2 = connection2.cursor()

cursor2.execute('''
CREATE TABLE IF NOT EXISTS vegs_fruits(
    name TEXT NOT NULL,
    type TEXT CHECK (type = 'vegetable' OR type = 'fruit'),
    colour TEXT NOT NULL,
    calories INTEGER NOT NULL,
    description TEXT NOT NULL
);
''')

# cursor2.executemany('''INSERT INTO vegs_fruits (name, type, colour, calories, description) VALUES (?, ?, ?, ?, ?)''',
# [("Apple", "fruit", "red", 52, "A sweet and crunchy fruit, rich in fiber and vitamins."),
# ("Banana", "fruit", "yellow", 89, "A soft, sweet fruit high in potassium."),
# ("Strawberry", "fruit", "red", 32, "A juicy and aromatic berry rich in vitamin C."),
# ("Cherry", "fruit", "red", 50, "A small, sweet fruit with a pit inside."),
# ("Pineapple", "fruit", "yellow", 50, "A tropical fruit with a spiky skin and juicy interior."),
# ("Mango", "fruit", "yellow", 60, "A tropical fruit with a sweet, fibrous pulp."),
# ("Watermelon", "fruit", "red", 30, "A refreshing fruit with high water content."),
# ("Raspberry", "fruit", "red", 53, "A delicate berry rich in antioxidants."),
# ("Lemon", "fruit", "yellow", 29, "A sour citrus fruit rich in vitamin C."),
# ("Peach", "fruit", "yellow", 39, "A juicy, fragrant fruit with soft skin."),
# ("Tomato", "vegetable", "red", 18, "A juicy vegetable often used in salads and sauces."),
# ("Red Bell Pepper", "vegetable", "red", 31, "A sweet pepper commonly eaten raw or cooked."),
# ("Carrot", "vegetable", "orange", 41, "A crunchy root vegetable high in beta-carotene."),
# ("Corn", "vegetable", "yellow", 86, "A starchy vegetable commonly eaten grilled or boiled."),
# ("Pumpkin", "vegetable", "yellow", 26, "A large vegetable often used in soups and desserts."),
# ("Beetroot", "vegetable", "red", 43, "A root vegetable rich in iron and fiber."),
# ("Sweet Potato", "vegetable", "orange", 86, "A nutritious root vegetable with a sweet taste."),
# ("Radish", "vegetable", "red", 16, "A crunchy vegetable with a slightly spicy flavor."),
# ("Yellow Bell Pepper", "vegetable", "yellow", 27, "A mild and sweet vegetable used in various dishes."),
# ("Cabbage", "vegetable", "green", 25, "A leafy vegetable often used in salads and soups.")])

print('\nВідображення усіх овочів з калорійністю, менше вказаної.')
cursor2.execute("SELECT * FROM vegs_fruits WHERE calories < 50 AND type = 'vegetable'")
vegs_calories_less_50 = cursor2.fetchall()
for x in vegs_calories_less_50:
    print(*x)

print('\nВідображення усіх фруктів з калорійністю у вказаному діапазоні.')
cursor2.execute("SELECT * FROM vegs_fruits WHERE calories BETWEEN 30 AND 60 AND type = 'fruit'")
fruits_calories_30_60 = cursor2.fetchall()
for x in fruits_calories_30_60:
    print(*x)

print('\nВідображення усіх овочів, у назві яких є вказане слово. Наприклад, слово: Pepper.')
cursor2.execute("SELECT * FROM vegs_fruits WHERE name LIKE '%pepper%' AND type = 'vegetable'")
vegs_name_pepper = cursor2.fetchall()
for x in vegs_name_pepper:
    print(*x)

print('\nВідображення усіх овочів та фруктів, у короткому описі яких є вказане слово. Наприклад, слово: vitamin.')
cursor2.execute("SELECT * FROM vegs_fruits WHERE description LIKE '%vitamin%'")
description_vitamin = cursor2.fetchall()
for x in description_vitamin:
    print(*x)

print('\nПоказати усі овочі та фрукти жовтого або червоного кольору.')
cursor2.execute("SELECT * FROM vegs_fruits WHERE colour = 'red' OR 'yellow'")
red_yellow = cursor2.fetchall()
for x in red_yellow:
    print(*x)

connection2.commit()
connection2.close()
