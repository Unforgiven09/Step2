# 1. Реалізуйте клас для побудови автомобіля, де можна задати такі характеристики:
# Марка автомобіля (наприклад, "Tesla", "BMW").
# Тип кузова (наприклад, "седан", "позашляховик").
# Колір.
# Тип двигуна (наприклад, "електричний", "дизельний", "бензиновий").
# Кількість дверей.
# Наявність додаткових опцій (наприклад, "панорамний дах", "шкіряний салон", "автопілот").
# Завдання:
# Реалізуйте клас Car для представлення автомобіля.
# Реалізуйте клас CarBuilder, який дозволяє поетапно будувати автомобіль.
# Напишіть клас Director, який керує побудовою автомобіля.
# Продемонструйте тестування створених класів, побудувавши кілька автомобілів із різними характеристиками.
from abc import ABC, abstractmethod


class CarBuilderBase(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _set_brand(self, brand):
        pass

    @abstractmethod
    def _set_colour(self, colour):
        pass

    @abstractmethod
    def _set_base(self, base):
        pass

    @abstractmethod
    def _set_engine(self, engine):
        pass

    @abstractmethod
    def _set_doors(self, doors):
        pass

    @abstractmethod
    def _set_extra(self, key, value):
        pass


class CarBuilder(CarBuilderBase):
    def __init__(self):
        self._info = {'brand': '', 'colour': '', 'base': '', 'engine': '', 'doors': ''}
        self._extra = {}

    def _set_brand(self, brand):
        self._info['brand'] = brand

    def _set_colour(self, colour):
        self._info['colour'] = colour

    def _set_base(self, base):
        self._info['base'] = base

    def _set_engine(self, engine):
        self._info['engine'] = engine

    def _set_doors(self, doors):
        self._info['doors'] = doors

    def _set_extra(self, key, value):
        self._extra[key] = value


class Car(CarBuilder):
    def show_info(self):
        print(f"This car is {self._info['brand']} brand, {self._info['colour']} {self._info['base']}, with"
              f" {self._info['engine']} engine and {self._info['doors']} doors!")
        if self._extra:
            print('This car also has additional characteristics:')
            for x, y in self._extra.items():
                print(x, ':', y)


class Director(Car):
    def set_info(self, brand, colour, base, engine, doors):
        self._set_brand(brand)
        self._set_colour(colour)
        self._set_base(base)
        self._set_engine(engine)
        self._set_doors(doors)

    def set_extra(self, **kwargs):
        for x, y in kwargs.items():
            self._set_extra(x, y)


car1 = Director()
car1.set_info('Tesla', 'black', '\'Cybertrack\'', 'electric', 5)
car1.set_extra(salon='eco leather', parktronic='auto')
car1.show_info()

car2 = Director()
car2.set_info('Ferrari', 'red', '\'Daytona\'', 'gasoline', 3)
car2.set_extra(transmission='auto')
car2.set_extra(salon='awsome!')
car2.set_extra(prestige='+100500 aura!')
car2.show_info()


# Завдання 2
# Створіть додаток для приготування пасти. Додаток має вміти створювати щонайменше три види пасти.
# Класи різної пасти мають містити такі методи:
# Тип пасти;
# Соус;
# Начинка;
# Добавки.
# Для реалізації використовуйте твірні патерни.


class PastaCreator(ABC):
    _pasta = ''
    _souse = ''
    _filler = ''
    _extra = ''

    @abstractmethod
    def pasta(self):
        pass

    @abstractmethod
    def souse(self):
        pass

    @abstractmethod
    def filler(self):
        pass

    @abstractmethod
    def extra(self):
        pass


class CustomPasta(PastaCreator):
    def pasta(self):
        pasta_all = [['Spaghetti', 'Fettuccine', 'Linguine', 'Capellini', 'Bavette'], # long
                     ['Penne', 'Fusilli', 'Rigatoni', 'Farfalle', 'Orecchiette'], # short
                     ['Ditali', 'Orzo', 'Cavatelli']] # small
        p_type = int(input('Choose type of pasta (long, short, small): '))
        p_sort = int(input(f'Choose sort of pasta {pasta_all[p_type-1]}: '))
        self._pasta = pasta_all[p_type-1][p_sort-1]

    def souse(self):
        souse_all = [['Marinara', 'Amatriciana', 'Puttanesca', 'Bolognese'], # tomato
                     ['Alfredo', 'Carbonara', 'Gorgonzola'], # cream
                     ['Aglio e Olio', 'Pesto', 'Cacio e Pepe']] # oil
        s_base = int(input('Choose base of souse (tomato, cream, oil): '))
        s_sort = int(input(f'Choose sort of souse {souse_all[s_base - 1]}: '))
        self._souse = souse_all[s_base - 1][s_sort - 1]

    def filler(self):
        fillers = ['Pork', 'Beef', 'Chicken', 'Lamb']
        choice = int(input(f'Choose your filler {fillers}: '))
        self._filler = fillers[choice - 1]

    def extra(self):
        self._extra = input("Add anything you want: ")

    def __str__(self):
        info = f'You chose {self._pasta} with {self._souse} souse and {self._filler} filler. '
        if self._extra:
            info += f"Also you want to add {self._extra}! "
        return info + "Great choice! Bon appetite!"


p = CustomPasta()
p.pasta()
p.souse()
p.filler()
p.extra()
print(p)
