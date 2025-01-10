# Створіть (або використайте раніше створений) клас «Дріб». Використовуючи перевантаження операторів, реалізуйте для
# нього арифметичні операції для роботи з дробами (операції +, -, *, /)

class Fractional:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __mul__(self, other):
        return self.x * other.x, self.y * other.y

    def __truediv__(self, other):
        return self.x / other.x, self.y / other.y


# Створіть клас «Бібліотека». Клас призначений для збереження інформації про бібліотеку (назва, адреса,  кількість
# книг і т.д.). Реалізуйте потрібні для класу способи. Використовуючи перевантаження операторів, реалізуйте для нього
# наступні арифметичні операції:
# + — додає до кількості книг вказане  значення;
# - — віднімає з кількості книг вказане значення;
# += —додає до кількості книг вказане  значення;
# -= — віднімає з кількості книг вказане  значення.
# Використовуючи перевантаження операторів,  реалізуйте (порівняння за кількістю книг):
# <;
# >;
# <=;
# >=;
# ==;
# !=


class Library:
    def __init__(self, name, address, books_amount):
        self.name = name
        self.address = address
        self.books_amount = books_amount

    def __add__(self, other):
        self.books_amount += other

    def __sub__(self, other):
        self.books_amount -= other

    def __iadd__(self, other):
        self.__add__(other)

    def __isub__(self, other):
        self.__sub__(other)

    def __eq__(self, other):
        return self.books_amount == other

    def __ne__(self, other):
        return self.books_amount != other

    def __gt__(self, other):
        return self.books_amount > other

    def __lt__(self, other):
        return self.books_amount < other

    def __ge__(self, other):
        return self.books_amount >= other

    def __le__(self, other):
        return self.books_amount <= other

# Створіть клас Date, який міститиме інформацію про дату (день, місяць, рік). За допомогою механізму перевантаження
# операторів визначте операцію різниці двох дат (результат у вигляді кількості днів між датами), а також операцію
# збільшення дати на певну кількість днів.


class Date:
    __slots__ = ['day', 'month', 'year']

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __sub__(self, other):
        return f"Difference is {other.year - self.year} years, {other.month - self.month} months, {other.day - self.day} days."

    def __add__(self, other):
        a = other % 30
        b = other // 30
        c = b // 12
        return self.day + a, self.month + b, self.year + c


abc = Date(1, 1, 2000)
print(abc + 396)