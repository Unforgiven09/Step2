# Створити три класи: Кішка (Cat), Собака (Dog) та Корова (Cow).Визначити такі атрибути об'єкта:ім'я (__name)вік
# (__age)колір (__color)Створити конструктор з трьома параметрами та три властивості(тільки гетери)

class Animal:
    def __init__(self, name, age, color):
        self._name = name
        self._age = age
        self._color = color

    def name(self):
        return self._name

    def age(self):
        return self._age

    def color(self):
        return self._color


class Cat(Animal):
    def __init__(self, name, age, color, voice_line):
        super().__init__(name, age, color)
        self._voice = voice_line

    def voice(self):
        return f"{self._name} says {self._voice}"


class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def voice(self, voice_line):
        return f"{self._name} says {voice_line}"


class Cow(Animal):
    def __init__(self, name, age, color, voice_line):
        super().__init__(name, age, color)
        self._voice = voice_line

    def voice(self):
        if self._voice == "Mu":
            return f"{self._name} is default cow and says 'Mu'"
        else:
            return f"{self._name} is not default cow and says {self._voice}"


# Створіть клас Passport (паспорт), який міститиме паспортну інформацію про громадянина заданої країни.
# За допомогою механізму успадкування реалізуйте клас ForeignPassport (закордонний паспорт), похідний від Passport.
# Нагадаємо, що закордонний паспорт містить, крім паспортних даних, дані про візи і номер закордонного паспорта.
# Кожен із класів має містити необхідні методи.


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

    def get_info(self):
        return super().get_info() + f'''Foreign country: {self._foreign_country}
Foreign passport ID: {self._foreign_passport_id}
Visa ID: {self._visa_id}
Visa validation: {self.is_visa()}
'''


ivan = ForeignPassport('Ivan', 32, 12345678, 98765432)
ivan.set_visa(111111, 2030)
print(ivan.get_info())