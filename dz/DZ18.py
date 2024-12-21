# Завдання 1
# Реалізуйте клас «Людина». Збережіть у класі: ПІБ, дату народження, контактний телефон, місто, країну, домашню адресу.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
# Додати метод is_major, який повертає True, якщо людина повнолітня (більше або одно 18 років) інакше False.


class Human:
    __fullName = None
    __birthday = None
    __tel = None
    __city = None
    __country = None
    __address = None

    def __init__(self, fullName):
        self.__fullName = fullName

    def change_full_Name(self, newName):
        self.__fullName = newName

    def change_birthday(self):
        try:
            day = int(input('Enter day of birth: '))
            month = int(input('Enter month of birth: '))
            year = int(input('Enter year of birth: '))
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if not 0 < day < 32:
                    raise Exception('In this month day should be in range from 1 to 31')
            elif month in [4, 6, 9, 11]:
                if not 0 < day < 31:
                    raise Exception('In this month day should be in range from 1 to 30')
            elif month == 2:
                if year % 4 == 0:
                    if not 0 < day < 30:
                        raise Exception('In this month day should be in range from 1 to 29')
                else:
                    if not 0 < day < 29:
                        raise Exception('In this month day should be in range from 1 to 28')
            else:
                raise Exception('Month should be in range from 1 to 12')
            self.__birthday = {'day': day, 'month': month, 'year': year}
        except ValueError:
            print('Use integers only')
        except Exception as ex:
            print(ex)

    def change_tel(self):
        self.__tel = int(input('Enter telephone number: '))

    def change_country(self):
        self.__country = input('Enter country name: ')

    def change_city(self):
        self.__city = input('Enter city name: ')

    def change_address(self):
        self.__address = input('Enter address: ')

    def show_info(self):
        info = [self.__fullName, self.__birthday, self.__tel, self.__country, self.__city, self.__address]
        for x in info:
            if x is not None:
                print(x)

    def is_major(self):
        try:
            if self.__birthday is not None:
                return True if 2024 - self.__birthday['year'] >= 18 else False
            else:
                raise Exception('First add birthday (.changeBirthday)')
        except Exception as ex:
            print(ex)


# Завдання 2
# Створіть клас «Місто». Збережіть у класі: назву міста, назву регіону, назву країни, кількість жителів у місті,
# поштовий індекс міста,
# телефонний код міста. Реалізуйте методи класу для введення-виведення даних та інших операцій.
# Написати метод is_valid_zipcode, який повертає True якщо __zipcode містить 5 цифр.


class City:
    def __init__(self, name, reg, country, population, zipcode):
        self.__name = name
        self.__reg = reg
        self.__country = country
        self.__population = population
        self.__zipcode = zipcode

    def show_info(self):
        info = {'name': self.__name, 'region': self.__reg, 'countru': self.__country,
                'population': self.__population, 'zipcode': self.__zipcode}
        for x in info:
            print(f'{x}')

    def is_valid_zipcode(self):
        return True if len(self.__zipcode) == 5 else False

    def change_info(self):
        item = input('What to change? ')
        if item == 'name':
            self.__name = item
        elif item == 'region':
            self.__reg = item
        elif item == 'country':
            self.__country = item
        elif item == 'population':
            self.__population = item
        elif item == 'zipcode':
            self.__zipcode = item
        else:
            print(f'{item} is not a parameter')


# Завдання 3
# Створіть клас «Країна». Збережіть у класі: назву країни, назву континенту, кількість жителів країни,
# телефонний код країни, назву столиці,
# назву міст країни. Реалізуйте методи класу для введення-виведення даних та інших операцій.


class Country:
    __cities = []

    def __init__(self):
        self.__name = input('Enter country name: ')
        self.__continent = input('Enter country continent name: ')
        self.__population = input('Enter country population: ')
        self.__tel_code = input('Enter country telephone code: ')
        self.__capital = input('Enter country capital city name: ')

    def add_new_city(self):
        new_city = input('Enter new city name')
        if new_city not in self.__cities:
            self.__cities.append(new_city)


# Завдання 4
# Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини,
# ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.


class Car:
    __year = 'no info'
    __engine_volume = 'no info'
    __colour = 'no info'
    __price = 'no info'

    def __init__(self, model, mark):
        self.__model = model
        self.__mark = mark

    def year(self):
        try:
            action = input('Enter "set" or "show" to work with year: ')
            if action == 'set':
                self.__year = int(input('Enter year of production: '))
                print(f'New year of production: {self.__year}')
            elif action == 'show':
                print(f'Year of production: {self.__year}')
            else:
                raise Exception('"set" or "show" ONLY')
        except ValueError:
            print('Integers only!')
        except Exception as ex:
            print(ex)

    def engine_volume(self):
        try:
            action = input('Enter "set" or "show" to work with engine volume: ')
            if action == 'set':
                self.__engine_volume = int(input('Enter engine volume: '))
                print(f'New engine volume: {self.__engine_volume}')
            elif action == 'show':
                print(f'Engine volume: {self.engine_volume}')
            else:
                raise Exception('"set" or "show" ONLY')
        except ValueError:
            print('Integers only!')
        except Exception as ex:
            print(ex)

    def colour(self):
        try:
            action = input('Enter "set" or "show" to work with colour: ')
            if action == 'set':
                self.__colour = input('Enter year of production: ')
                print(f'Colour: {self.__colour}')
            elif action == 'show':
                print(f'Colour: {self.__colour}')
            else:
                raise Exception('"set" or "show" ONLY')
        except Exception as ex:
            print(ex)

    def price(self):
        try:
            action = input('Enter "set" or "show" to work with price: ')
            if action == 'set':
                self.__price = int(input('Enter price: '))
                print(f'New price: {self.__price}')
            elif action == 'show':
                print(f'Price: {self.__price}')
            else:
                raise Exception('"set" or "show" ONLY')
        except ValueError:
            print('Integers only!')
        except Exception as ex:
            print(ex)


# Завдання 5
# Реалізуйте клас «Книга». Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.


class Book:
    def __init__(self):
        self.__name = input('Set name of book: ')
        self.__author = input('Set author: ')
        self.__year = int(input('Set year of publishing: '))
        self.__publisher = input('Set publisher: ')
        self.__genre = input('Set genre: ')
        self.__price = None

    def set_price(self):
        self.__price = int(input('Set new price'))

    def name(self):
        return self.__name

    def author(self):
        return self.__author

    def year(self):
        return self.__year

    def publisher(self):
        return self.__publisher

    def genre(self):
        return self.__genre

    def price(self):
        return self.__price
