# Потрібно створити клас "Фільм", в якому використовуватиметься клас-метод з ім'ям "середній_рейтинг",
# який буде обчислювати середній рейтинг всіх фільмів, створених з використанням цього класу.
# реалізуйте функцію для виведення рейтингу всіх фільмів та функцію для виведення імен.
import random


class AllFilms:
    __avg_rate = 0
    __rates = []
    __names = []

    @classmethod
    def add_film(cls, name, rate):
        cls.__names.append(name)
        cls.__rates.append(rate)

    @classmethod
    def avg_rate(cls):
        cls.__avg_rate = sum(cls.__rates) / len(cls.__rates)

    @classmethod
    def show_all_films(cls):
        for x in range(len(cls.__names)):
            print(f'Film name: {cls.__names[x]}, rate: {cls.__rates[x]}')
        print(f'Avg rate = {cls.__avg_rate}')


class Film(AllFilms):
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        AllFilms.add_film(name, rate)
        AllFilms.avg_rate()


class Cartoon(AllFilms):
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        AllFilms.add_film(name, rate)
        AllFilms.avg_rate()


a = Film("Godfather", 10)
b = Film("Batman", 8)
c = Film("Green mile", 12)
d = Film("Green elephant", 3)
e = Cartoon('Frozen', 10)
f = Cartoon('Moana', 11)
AllFilms.show_all_films()

# Використовуючи механізм множинного успадкування, розробіть клас "Людина".
# Мають бути класи "Мозок", "Серце", "Ноги" і т.д.


class Brain:
    def __init__(self, amount_of_cerebral_gyrus):
        self.amount_of_cerebral_gyrus = amount_of_cerebral_gyrus

    def think(self, question_difficulty):
        return f'to solve question you need {question_difficulty / self.amount_of_cerebral_gyrus} sec'


class Heart:
    def __init__(self, blood_volume, pump_speed):
        self.blood_volume = blood_volume
        self.pump_speed = pump_speed

    def heart_working(self, beats_per_min):
        print(f'Heart uses {self.blood_volume * beats_per_min} liters of blood and works with speed {self.pump_speed}')


class Legs:
    legs = 2

    @staticmethod
    def walk():
        print("Step")
        for x in range(random.randint(5, 10)):
            print("by step")
        print("and stop!")


class Hands:
    hands = 2

    @staticmethod
    def clap():
        for x in range(random.randint(5, 10)):
            print("Clap!")


class Hair:
    def __init__(self, length, colour):
        self.length = length
        self.colour = colour


class Human(Brain, Heart, Legs, Hair, Hands):
    def __init__(self, amount_of_cerebral_gyrus, blood_volume, pump_speed, length, colour, name):
        Brain.__init__(self, amount_of_cerebral_gyrus)
        Heart.__init__(self, blood_volume, pump_speed)
        Hair.__init__(self, length, colour)
        self.name = name

    def info(self):
        print(f'This human name is {self.name}', end="")
        if 100 < self.amount_of_cerebral_gyrus < 1000:
            print(", he is avg clever", end="")
        elif self.amount_of_cerebral_gyrus >= 1000:
            print(", he is very clever", end="")
        else:
            print(", he is not so clever", end="")
        if self.length > 40:
            print(f", with long {self.colour} hair", end="")
        elif self.length > 20:
            print(f", with medium {self.colour} hair", end="")
        elif self.length > 0:
            print(f", with short {self.colour} hair", end="")
        else:
            print(f", bald", end="")
        print(" and very kind person!")


person = Human(1001, 0.1, 5, 25, 'black', 'Joe')
person.info()
person.clap()
person.heart_working(90)
person.walk()