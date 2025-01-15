# Завдання: Реалізація системи геометричних фігур із використанням абстрактних класів
# Опис завдання:
# Вам потрібно створити абстрактний клас Shape, який буде представляти загальний вигляд для
# геометричних фігур. У цьому класі потрібно визначити такі абстрактні методи:
#
# area() — обчислення площі.
# perimeter() — обчислення периметра.
# description() — виведення текстового опису фігури.
# Потім створіть кілька конкретних класів, які наслідують абстрактний клас Shape:
#
# Circle — коло, задане радіусом.
# Rectangle — прямокутник, заданий шириноюта висотою.
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def description(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.name = 'circle'
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return self.radius * 2 * 3.14

    def description(self):
        return f"{self.name} has area {self.area()} and perimeter {self.perimeter()}"


class Rectangle(Shape):
    def __init__(self, h, w):
        self.name = 'rectangle'
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return (self.w + self.h) * 2

    def description(self):
        return f"{self.name} has area {self.area()} and perimeter {self.perimeter()}"

