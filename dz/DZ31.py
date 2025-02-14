import sqlite3

# Завдання 1
# Створіть базу для зберігання оцінок студентів. Всередині бази даних створіть таблицю "Оцінки студентів".
# Потрібно зберігати таку інформацію:
# ■ ПІБ студента;
# ■ Місто;
# ■ Країна;
# ■ Дата народження;
# ■ Електронна адреса;
# ■ Контактний телефон;
# ■ Назва групи;
# ■ Середня оцінка за рік з усіх предметів;
# ■ Назва предмета з мінімальною, середньою оцінкою;
# ■ Назва предмета з максимальною, середньою оцінкою.

connection1 = sqlite3.connect('DZ31.db')
cursor1 = connection1.cursor()

cursor1.execute('''
CREATE TABLE IF NOT EXISTS students_marks(
    full_name TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    bday DATETIME NOT NULL,
    email TEXT,
    tel INTEGER NOT NULL,
    group TEXT NOT NULL,
    avg_mark REAL NOT NULL,
    subject_min_avg_mark TEXT NOT NULL,
    subject_max_avg_mark TEXT NOT NULL
);
''')

connection1.commit()
connection1.close()

# Завдання 2
# Створіть базу даних Лікарня (Hospital), яка міститиме інформацію про обстеження, які проводяться в лікарні.
# Обстеження, які проводяться в лікарні, представлені у вигляді таблиці Обстеження (Examinations), в якій зібрано
# основну інформацію: назва обстеження, день тижня, коли проводиться обстеження, а також час початку та завершення.
# Також у базі даних є інформація про персонал лікарні, яка зберігається в таблиці Лікарі (Doctors). Дані про
# відділення та захворювання містяться в таблицях Відділення (Departments) та Захворювання (Diseases) відповідно.
# Опис палат зберігається в таблиці Палати (Wards).
# Таблиці
# Нижче наведено детальний опис структури кожної таблиці.

# Відділення (Departments)

# Ідентифікатор (Id). Унікальний ідентифікатор відділення.
#   Тип даних — int.
#   Автоприріст.
#   Не містить null-значення.
#   Первинний ключ.
# Корпус (Building). Номер корпусу, в якому знаходиться відділення.
#   Тип даних — int.
#   Не містить null-значення.
#   Має бути в діапазоні від 1 до 5.
# Фінансування (Financing). Фонд фінансування відділення.
#   Тип даних для зберігання грошових значень.
#   Не містить null-значення.
#   Не може бути менше, ніж 0.
#   Значення за замовчуванням — 0.
# Назва (Name). Назва відділення.
#   Тип даних — nvarchar(100).
#   Не містить null-значення.
#   Не може бути порожньою.
#   Має бути унікальною.
#
# Захворювання (Diseases)
#
# Ідентифікатор (Id). Унікальний ідентифікатор захворювання.
#   Тип даних — int.
#   Автоприріст.
#   Не містить null-значення.
#   Первинний ключ.
# Назва (Name). Назва захворювання.
#   Тип даних — nvarchar(100).
#   Не містить null-значення.
#   Не може бути порожньою.
#   Має бути унікальною.
#   Ступінь тяжкості (Severity). Ступінь тяжкості захворювання.
#   Тип даних — int.
#   Не містить null-значення.
#   Не може бути менше, ніж 1.
#   Значення за замовчуванням — 1.
#
# Лікарі (Doctors)
#
# Ідентифікатор (Id). Унікальний ідентифікатор лікаря.
#   Тип даних — int.
#   Автоприріст.
#   Не містить null-значення.
#   Первинний ключ.
# Ім'я (Name). Ім'я лікаря.
#   Тип даних — nvarchar(max).
#   Не містить null-значення.
#   Не може бути порожнє.
#   Телефон (Phone). Телефонний номер лікаря.
#   Тип даних — char(10).
#   Може містити null-значення.
# Ставка (Salary). Ставка лікаря.
#   Тип даних для зберігання грошових значень.
#   Не містить null-значення.
#   Не може бути меншою або дорівнювати 0.
# Прізвище (Surname). Прізвище лікаря.
#   Тип даних — nvarchar(max).
#   Не містить null-значення.
#   Не може бути порожнє.
#
# Обстеження (Examinations)
#
# Ідентифікатор (Id). Унікальний ідентифікатор обстеження.
#   Тип даних — int.
#   Автоприріст.
#   Не містить null-значення.
#   Первинний ключ.
# День тижня (DayOfWeek). День тижня, коли проводиться обстеження.
#   Тип даних — int.
#   Не містить null-значення.
#   Має бути в діапазоні від 1 до 7.
#   Час завершення (EndTime). Час завершення обстеження.
#   Тип даних для зберігання часу.
#   Не містить null-значення.
#   Має бути більше, ніж час початку обстеження.
# Назва (Name). Назва обстеження.
#   Тип даних — nvarchar(100).
#   Не містить null-значення.
#   Не може бути порожньою.
#   Має бути унікальною.
#   Час початку (StartTime). Час початку обстеження.
#   Тип даних для зберігання часу.
#   Не містить null-значення.
#   Має бути в діапазоні від 8:00 до 18:00.
#
# Палати (Wards)
#
# Ідентифікатор (Id). Унікальний ідентифікатор.
#  Тип даних — int.
#  Автоприріст.
#  Не містить null-значення.
#  Первинний ключ.
# Корпус (Building). Номер корпусу, де знаходиться палата.
#  Тип даних — int.
#  Не містить null-значення.
#  Має бути в діапазоні від 1 до 5.
# Поверх (Floor). Номер поверху, на якому знаходиться палата.
#  Тип даних — int.
#  Не містить null-значення.
#  Не може бути менше, ніж 1.
# Назва (Name). Назва палати.
#  Тип даних — nvarchar(20).
#  Не містить null-значення.
#  Не може бути порожньою.
#  Має бути унікальною.


connection2 = sqlite3.connect('DZ31.db')
cursor2 = connection2.cursor()

cursor2.execute('''
CREATE TABLE IF NOT EXISTS departments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    building INTEGER NOT NULL CHECK (building > 0 OR building < 6),
    financing REAL NOT NULL DEFAULT 0.0 CHECK (financing >= 0),
    name NVARCHAR(100) UNIQUE NOT NULL CHECK (name <> '')
);
''')

cursor2.execute('''
CREATE TABLE IF NOT EXISTS diseases(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name NVARCHAR(100) UNIQUE NOT NULL CHECK (name <> ''),
    severity INTEGER NOT NULL CHECK (financing > 0) DEFAULT 1
);
''')

cursor2.execute('''
CREATE TABLE IF NOT EXISTS doctors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name NVARCHAR(max) NOT NULL CHECK (name <> ''),
    surname NVARCHAR(max) NOT NULL CHECK (surname <> ''),
    phone NVARCHAR(10),
    salary REAL NOT NULL CHECK (salary > 0)
);
''')

cursor2.execute('''
CREATE TABLE IF NOT EXISTS examinations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day_of_week INTEGER NOT NULL CHECK (day_of_week > 0 OR day_of_week < 8),
    name NVARCHAR(100) NOT NULL UNIQUE,
    start_time TIMESTAMP NOT NULL CHECK (start_time >= 08:00 OR start_time <= 18:00),
    end_time TIMESTAMP NOT NULL,
    CHECK(end_time > start_time)
);
''')

cursor2.execute('''
CREATE TABLE IF NOT EXISTS wards(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    building INTEGER NOT NULL CHECK (building > 0 OR day_of_week < 6),
    floor INTEGER NOT NULL CHECK (floor > 0),
    name NVARCHAR(20) NOT NULL UNIQUE CHECK (name <> '')
);
''')

connection2.commit()
connection2.close()
