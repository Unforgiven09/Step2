# Завдання 1
# Створіть клас Passport (паспорт), який міститиме паспортну інформацію про громадянина заданої країни.
# За допомогою механізму успадкування реалізуйте клас ForeignPassport (закор­дон­ний паспорт), похідний від Passport.
# Нагадаємо, що закордонний паспорт містить, крім паспортних даних, дані про візи і номер закордонного паспорта.
# Кожен із класів має містити необхідні методи.
import random
import time


class Passport:
    _native_country = "Ukraine"

    def __init__(self, name, age, passport_id):
        self._name = name
        self._age = age
        self._passport_id = passport_id

    def get_info(self):
        return f'''Passport ID: {self._passport_id}
Name: {self._name}
Age: {self._age}
Native county: {self._native_country}
'''


class ForeignPassport(Passport):
    _foreign_country = None
    _visa_id = None
    _visa_year = None

    def __init__(self, name, age, passport_id, foreign_passport_id):
        super().__init__(name, age, passport_id)
        self._foreign_passport_id = foreign_passport_id

    def set_visa(self, visa_id, visa_year):
        self._visa_id = visa_id
        self._visa_year = visa_year

    def is_visa(self):
        if int(self._visa_year) > 2024:
            return 'visa is valid'

    def foreign_country(self):
        self._foreign_country = input('Enter foreign country name: ')

    def get_info(self):
        return super().get_info() + f'''Foreign country: {self._foreign_country}
Foreign passport ID: {self._foreign_passport_id}
Visa ID: {self._visa_id}
Visa validation: {self.is_visa()}
'''


# Завдання 2
# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас CoffeeMachine (містить інформацію про кавомашину),
# клас Blender (містить інформацію про блендер), клас MeatGrinder (містить інформацію про м'ясорубку).
# Кожен із класів має містити необхідні для роботи методи.


class Device:
    _time_to_work = None
    _material = None
    _colour = None

    def __init__(self, producer_name, producer_id, model, size, power):
        self._producer_name = producer_name
        self._producer_id = producer_id
        self._model = model
        self._size = size
        self._power = power

    def time_to_work(self):
        self._time_to_work = input("How long can it work before overheat? ")

    def material(self):
        self._material = input("What is main material? ")

    def colour(self):
        self._colour = input("What is the colour? ")

    def general_info(self):
        general_info = {'producer name': self._producer_name, 'producer id': self._producer_id, 'model': self._model,
                        'size': self._size, 'power': self._power, 'time to work': self._time_to_work,
                        'material': self._material, 'colour': self._colour}
        for x in general_info.keys():
            print(f'{x.capitalize()}: {general_info[x]}')


class CoffeeMachine(Device):
    def __init__(self, producer_name, producer_id, model, size, power, milling, volume):
        super().__init__(producer_name, producer_id, model, size, power)
        self._milling = milling
        self._volume = volume

    def general_info(self):
        super().general_info()
        add_info = {'milling': self._milling, 'volume': self._volume}
        for x in add_info.keys():
            print(f'{x.capitalize()}: {add_info[x]}')


class Blender(Device):
    def __init__(self, producer_name, producer_id, model, size, power, blades, volume):
        super().__init__(producer_name, producer_id, model, size, power)
        self._blades = blades
        self._volume = volume

    def general_info(self):
        super().general_info()
        add_info = {'blades': self._blades, 'volume': self._volume}
        for x in add_info.keys():
            print(f'{x.capitalize()}: {add_info[x]}')


class MeatGrinder(Device):
    def __init__(self, producer_name, producer_id, model, size, power, milling, blades):
        super().__init__(producer_name, producer_id, model, size, power)
        self._milling = milling
        self._blades = blades

    def general_info(self):
        super().general_info()
        add_info = {'milling': self._milling, 'blades': self._blades}
        for x in add_info.keys():
            print(f'{x.capitalize()}: {add_info[x]}')


# Завдання 3
# Створіть клас Ship, який містить інформацію про кораблі. За допомогою механізму успадкування реалізуйте клас Frigate
# (містить інформацію про фрегат), клас Destroyer (містить інформацію про есмінця), клас Cruiser (містить інформацію
# про крейсер). Кожен із класів має містити необхідні для роботи методи.


class Ship:
    _name = None
    _type = None
    _len = None
    _width = None
    _height = None
    _weight = None
    _crew_members = []
    _crew_num = 0
    _capitan = None

    def __init__(self, name):
        self._name = name

    def parameters(self):
        parameters = {'length': self._len, 'width': self._width, 'height': self._height, 'weight': self._weight}
        action = input('Choose set or show: ')
        if action.lower() == 'set':
            self._len = input(f'Set length: ')
            self._width = input(f'Set width: ')
            self._height = input(f'Set height: ')
            self._weight = input(f'Set weight: ')
        elif action.lower() == 'show':
            for x in parameters.keys():
                print(f'{x.capitalize()} = {parameters[x]}')
        elif action.lower() == "q":
            pass
        else:
            print('Enter only "set" or "show" ("q" to exit)')
            self.parameters()

    def crew(self):
        action = input('Choose set or show: ')
        if action.lower() == 'set':
            if not self._capitan:
                self._capitan = input("Capitan name is: ")
            elif self._capitan:
                new_cap = input(f'Capitan is {self._capitan}, change info? y/n: ')
                if new_cap == 'y':
                    self._capitan = input('Set new capitan name: ')
            while True:
                name = input("New crew member name (empty slot to quit):")
                if name:
                    self._crew_members.append(name)
                    self._crew_num = len(self._crew_members) + 1
                else:
                    break
        elif action.lower() == 'show':
            if self._crew_num > 0:
                print(f"Crew is {self._crew_num} people\nCapitan: {self._capitan}, others: ", end="")
                for x in self._crew_members:
                    print(x + ", ", end="")
            else:
                print("Crew info is empty")

    def info(self):
        return f'Ship name: {self._name}, ship type: {self._type}' if self._type is not None else f'Ship name: {self._name}'


class Frigate(Ship):
    def __init__(self, name):
        super().__init__(name)
        self._type = 'frigate'

    @staticmethod
    def shoot(self, cannon):
        if cannon == "turret":
            print("Turret is ready to fire!")
            print("TRA-TA", end="")
            for x in range(random.randint(20, 40)):
                time.sleep(0.3)
                print("-TA", end="")
            print("\nNEED TO RELOAD TURRET!!!")
        elif cannon == "aag":
            print("ANTI AIR GUN is ready to fire!")
            for x in range(random.randint(5, 10)):
                print("TRA-TA-TA")
                time.sleep(1)
            print("ANTI AIR GUN amo is out! RELOAD!")
        else:
            print(f"NO GUN {cannon} is attached!")


class Destroyer(Ship):
    def __init__(self, name):
        super().__init__(name)
        self._type = 'destroyer'

    @staticmethod
    def shoot(cannon):
        if cannon == "mortar":
            print("MORTAR is ready to fire!")
            print("CABOOOOM")
            time.sleep(10)
            print('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            {{{BAAAA_DAAAAAAA_BOOOOOOOOM}}}
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
            print("MORTAR GOT A HIT!!!")
        elif cannon == "missile":
            print("MISSILE LAUNCHER is ready to fire!")
            for x in range(random.randint(5, 10)):
                print("PSHEEEW")
                time.sleep(3)
            print("MISSILE LAUNCHER is out of missiles! RELOAD!")
        else:
            print(f"NO GUN {cannon} is attached!")


class Cruiser(Ship):
    def __init__(self, name):
        super().__init__(name)
        self._type = 'cruiser'

    @staticmethod
    def shoot(self, cannon):
        if cannon == "railgun":
            print("RAILGUN is ready to fire!")
            print("BLAAAAAAAAH")
            print("RAILGUN NEED NEW RAILS!!! and gun also))")
        elif cannon == "BFG":
            print('Need to import BFG from DOOM ETERNAL')
            print('if you see this - check out this cover https://www.youtube.com/watch?v=ak8-Mpb54JM')
        else:
            print(f"NO GUN {cannon} is attached!")


# Завдання 4
# Запрограмуйте клас Money (об'єкт класу оперує однією валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої частини грошей (долари, євро, гривні тощо) і поле для
# зберігання копійок (центи, євроценти, копійки тощо)
# Реалізуйте методи виведення суми на екран, задання значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для зменшення
# ціни на задане число. Для кожного з класів реалізуйте необхідні методи та поля.


class Money:
    __valid_currencies = ['dollar', 'euro', 'hryvnia']

    def __init__(self, currency, integer, fractional_part):
        try:
            if currency in self.__valid_currencies:
                self._currency = currency
            else:
                raise Exception("Currency should be 'dollar', 'euro' or 'hryvnia'!")
            if int(integer) >= 0:
                self._integer = int(integer)
            else:
                raise ValueError
            if 0 <= int(fractional_part) < 100:
                self._fractional_part = int(fractional_part)
            else:
                raise ValueError
        except ValueError:
            print('Integer and fractional part should be positive integers and fractional part should be in range 0-99')
        except Exception as ex:
            print(ex)

    def info(self):
        temp = self._integer + (self._fractional_part / 100)
        return f'{temp} {self._currency}s'


class Product:
    _price = ("currency", 0, 0)

    def __init__(self, name):
        self._name = name

    def set_price(self):
        try:
            currency = input("Enter currency name ('dollar', 'euro', 'hryvnia'): ")
            cost = float(input(f"Enter {self._name} price: "))
            discount = int(input("Set discount: "))
            cost = cost * (100 - discount) / 100
            value = []
            if currency.lower() in ['dollar', 'euro', 'hryvnia']:
                value.append(currency.lower())
            else:
                raise Exception("Wrong currency name")
            if cost > 0:
                integer = int(cost)
                fractional_part = int(cost * 100 % 100)
                value.append(integer)
                value.append(fractional_part)
            else:
                raise Exception("Wrong price!")
            self._price = tuple(value)
        except Exception as ex:
            print(ex)

    def info(self):
        temp = Money(*self._price)
        print(f"{self._name} costs {temp.info()}")


# Завдання 5
# Створіть клас для конвертування температури з Цельсія у Фаренгейт, і навпаки. У класі має знаходитися два статичні
# методи: для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має
# розрахувати кількість підрахунків температури та повернути це значення статичним методом.


class TemperatureConvertor:
    __usages = 0

    def __usage(func):
        def wrapper(self, *args, **kwargs):
            self.__usages += 1
            result = func(*args, **kwargs)
            return result
        return wrapper

    @__usage
    @staticmethod
    def c_to_f(temp_c):
        return temp_c * 9 / 5 + 32

    @__usage
    @staticmethod
    def f_to_c(temp_f):
        return (temp_f - 32) * 5 / 9

    def show_usages(self):
        print(f"Temperature converter was used {self.__usages} time(s).")


# Завдання 6
# Створіть клас для конвертування з метричної системи в англійську, та навпаки. Реалізуйте функціональність у вигляді 
# статичних методів. Обов'язково реалізуйте конвертування заходів довжини.


class MetricImperialConvertor:

    @staticmethod
    def length_convertor(amount, measure_in, measure_out):
        measure = ['millimetre', 'centimetre', 'metre', 'kilometre', 'inch', 'foot', 'yard', 'mile']
        measurement_info = [[1, 0.1, 0.001, 0.000001, 5/127, 5/1524, 5/4572, 1/1609344],
                            [10, 1, 0.01, 0.00001, 50/127, 50/1524, 50/4572, 10/1609344],
                            [1000, 100, 1, 0.001, 5000/127, 1250/381, 1250/1143, 125/201168],
                            [1000000, 100000, 1000, 1, 5000000/127, 1250000/381, 1250000/1143, 15625/25146],
                            [25.4, 2.54, 0.0254, 0.0000254, 1, 1/12, 1/36, 1/63360],
                            [304.8, 30.48, 0.3048, 0.0003048, 12, 1, 1/3, 1/5280],
                            [914.4, 91.44, 0.9144, 0.0009144, 36, 3, 1, 1/1760],
                            [1609344, 160934.4, 1609.344, 1.609344, 63360, 5280, 1760, 1]]

        return amount * measurement_info[measure.index(measure_in)][measure.index(measure_out)]

    @staticmethod
    def weight_convertor(amount, measure_in, measure_out):
        metric = ['gram', 'kilogram', 'tonne']
        imperial = ['ounce', 'pound']
        measurement_info = [[28.3495, 0.02835, 0.00002835],
                            [453.592, 0.45359, 0.00045359]]
        if measure_in in metric:
            x = metric.index(measure_in)
            y = imperial.index(measure_out)
            return amount / measurement_info[y][x]
        elif measure_in in imperial:
            x = imperial.index(measure_in)
            y = metric.index(measure_out)
            return amount * measurement_info[x][y]

    @staticmethod
    def volume_convertor(amount, measure_in, measure_out):
        metric = ['litre']
        imperial = ['pint', 'gallon']
        measurement_info = [[0.568],
                            [4.546]]
        if measure_in in metric:
            x = metric.index(measure_in)
            y = imperial.index(measure_out)
            return amount / measurement_info[y][x]
        elif measure_in in imperial:
            x = imperial.index(measure_in)
            y = metric.index(measure_out)
            return amount * measurement_info[x][y]

