# Завдання 1
# Створіть клас Airplane (Літак). За допомогою перевантаження операторів, реалізуйте:
# перевірку на рівність типів літаків (операція = =);
# збільшення та зменшення пасажирів у салоні літака (операції +, -, +=, -=);
# порівняння двох літаків за максимально можливою кількістю пасажирів на борту (операції >, <, <=, >=).

class Airplane:
    passengers_on_board = 0

    def __init__(self, name, plane_type, passengers):
        self.name = name
        self.plane_type = plane_type
        self.passengers = passengers

    def __str__(self):
        return f" {self.name} is a plane {self.plane_type} type with {self.passengers} passengers capacity, currently on board: {self.passengers_on_board}"

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    def __add__(self, other):
        self.passengers += other

    def __iadd__(self, other):
        self.passengers_on_board += other

    def __sub__(self, other):
        self.passengers -= other

    def __isub__(self, other):
        self.passengers_on_board -= other

    def __lt__(self, other):
        return self.passengers < other.passengers

    def __le__(self, other):
        return self.passengers <= other.passengers

    def __gt__(self, other):
        return self.passengers > other.passengers

    def __ge__(self, other):
        return self.passengers >= other.passengers

# Завдання 2
# Створіть клас Flat (Квартира). Реалізуйте перевантажені оператори:

# перевірку на рівність площ квартир (операція ==);
# перевірку на нерівність площ квартир (операція !=);
# порівняння двох квартир за ціною (операції >, <, <=, >=).


class Flat:
    def __init__(self, sq, price):
        self.sq = sq
        self.price = price

    def __str__(self):
        return f"This flat is {self.sq} sq metrs and {self.price}$ cost"

    def __eq__(self, other):
        return self.sq == other.sq

    def __ne__(self, other):
        return self.sq != other.sq

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

# Завдання 3
# Створіть базовий клас Shape для рисування плоских фігур. Визначте методи:

# Show() — виведення на екран інформації про фігуру;
# Save() — збереження фігури у файл;
# Load() — зчитування фігури з файлу.

# Визначте похідні класи:

# Square — квадрат із заданими з координатами лівого верхнього кута та довжиною сторони.
# Rectangle — прямокутник із заданими координатами верхнього лівого кута та розмірами.
# Circle — коло із заданими координатами центру та радіусом.
# Ellipse — еліпс із заданими координатами верхнього кута описаного навколо нього прямокутника зі сторонами,
# паралельними осям координат, та розмірами цього прямокутника.
# Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну фігуру.


class Shape:
    name = "dot"

    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def show(self):
        return f'{self.name}:{self.x1}:{self.y1}'

    def __str__(self):
        return self.show()

    def save(self):
        with open('Shapes', "a") as file:
            file.write(self.show() + "\n")

    @staticmethod
    def load():
        with open('Shapes') as file:
            for x in file.readlines():
                if 'dot' in x:
                    x = x[:-1]
                    x = x.split(":")
                    print(f"Figure name is {x[0]} with the coordinates {x[1]}:{x[2]}")
                elif "square" in x:
                    x = x[:-1]
                    x = x.split(":")
                    print(f"Figure name is {x[0]} with the coordinates of the upper left corner {x[1]}:{x[2]} and "
                          f"the length of the side = {x[3]}")
                elif "rectangle" in x:
                    x = x[:-1]
                    x = x.split(":")
                    print(f"Figure name is {x[0]} with the coordinates of the upper left corner {x[1]}:{x[2]} and "
                          f"the length of the first side = {x[3]} and second side = {x[4]}")
                elif "circle" in x:
                    x = x[:-1]
                    x = x.split(":")
                    print(f"Figure name is {x[0]} with the coordinates of the center {x[1]}:{x[2]} and "
                          f"the length of the radius = {x[3]}")
                elif "ellipse" in x:
                    x = x[:-1]
                    x = x.split(":")
                    print(f"Figure name is {x[0]} with the coordinates of the center {x[1]}:{x[2]} and"
                          f" the upper left corner {x[3]}:{x[4]} and "
                          f"the length of the first side = {x[5]} and second side = {x[6]}")


class Square(Shape):
    def __init__(self, x1, y1, side_len):
        super().__init__(x1, y1)
        self.name = 'square'
        self.side_len = side_len

    def show(self):
        return super().show() + f':{self.side_len}'

    @staticmethod
    def load():
        with open('Shapes') as file:
            flag = False
            for x in file.readlines():
                if "square" in x:
                    x = x[:-1]
                    x = x.split(":")
                    print(f"Figure name is {x[0]} with the coordinates of the upper left corner {x[1]}:{x[2]} and "
                          f"the length of the side = {x[3]}")
                    flag = True
            if not flag:
                print('No squares in data!')


class Rectangle(Shape):
    def __init__(self, x1, y1, side1_len, side2_len):
        super().__init__(x1, y1)
        self.name = 'rectangle'
        self.side1_len = side1_len
        self.side2_len = side2_len

    def show(self):
        return super().show() + f':{self.side1_len}:{self.side2_len}'

    @staticmethod
    def load():
        with open('Shapes') as file:
            flag = False
            for x in file.readlines():
                if "rectangle" in x:
                    x = x[:-1]
                    x = x.split(":")
                    print(f"Figure name is {x[0]} with the coordinates of the upper left corner {x[1]}:{x[2]} and "
                          f"the length of the first side = {x[3]} and second side = {x[4]}")
                    flag = True
            if not flag:
                print('No rectangles in data!')


class Circle(Shape):
    def __init__(self, x1, y1, radius):
        super().__init__(x1, y1)
        self.name = 'circle'
        self.radius = radius

    def show(self):
        return super().show() + f':{self.radius}'

    @staticmethod
    def load():
        with open('Shapes') as file:
            flag = False
            for x in file.readlines():
                if "circle" in x:
                    x = x[:-1]
                    x = x.split(":")
                    print(f"Figure name is {x[0]} with the coordinates of the center {x[1]}:{x[2]} and "
                          f"the length of the radius = {x[3]}")
                    flag = True
            if not flag:
                print('No circles in data!')


class Ellipse(Shape):
    def __init__(self, x1, y1, x2, y2, side1_len, side2_len):
        super().__init__(x1, y1)
        self.name = 'ellipse'
        self.x2 = x2
        self.y2 = y2
        self.side1_len = side1_len
        self.side2_len = side2_len

    def show(self):
        return super().show() + f':{self.x2}:{self.y2}:{self.side1_len}:{self.side2_len}'

    @staticmethod
    def load():
        with open('Shapes') as file:
            flag = False
            for x in file.readlines():
                if "ellipse" in x:
                    x = x[:-1]
                    x = x.split(":")
                    print(f"Figure name is {x[0]} with the coordinates of the center {x[1]}:{x[2]} and"
                          f" the upper left corner {x[3]}:{x[4]} and "
                          f"the length of the first side = {x[5]} and second side = {x[6]}")
                    flag = True
            if not flag:
                print('No ellipses in data!')


figure1 = Shape(0, 0)
figure1.save()
figure2 = Square(1, 1, 3)
figure2.save()
figure3 = Rectangle(2, 2, 4, 2)
figure3.save()
figure4 = Circle(1, 1, 3)
figure4.save()
Shape.load()
Square.load()
Ellipse.load()
