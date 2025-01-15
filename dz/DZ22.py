# Завдання: Реалізація системи геометричних фігур із використанням абстрактних класів
# Опис завдання:
# Вам потрібно створити абстрактний клас Shape, який буде представляти загальний вигляд для геометричних фігур.
# У цьому класі потрібно визначити такі абстрактні методи:
# area() — обчислення площі.
# perimeter() — обчислення периметра.
# description() — виведення текстового опису фігури.
# Потім створіть кілька конкретних класів, які наслідують абстрактний клас Shape:
# Circle — коло, задане радіусом.
# Rectangle — прямокутник, заданий шириною та висотою.
# Triangle — трикутник, заданий довжинами трьох сторін.
# У кожному з цих класів реалізуйте абстрактні методи відповідно до специфіки фігури.
# Додаткові вимоги:
# У класі Triangle реалізуйте перевірку, чи існує трикутник з заданими сторонами (умова трикутника).
# Створіть клас, в якому описано список фігур, обчислює їх площу та периметр і виводить результати на екран.
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


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.name = 'triangle'
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    def description(self):
        return f"{self.name} has area {self.area()} and perimeter {self.perimeter()}"

    def is_valid(self):
        return True if self.a + self.b > self.c and self.a + self.c > self.b and self.a < self.b + self.c else False


class WorkWithShapes:
    data = []

    def __init__(self, *args):
        for x in args:
            self.data.append(x)

    def areas(self):
        print("All areas:")
        for x in self.data:
            print(x.area())

    def perimeters(self):
        print("All perimeters:")
        for x in self.data:
            print(x.perimeter())

    def descriptions(self):
        for x in self.data:
            if isinstance(x, Shape):
                print(x.description())


# o1 = Triangle(3, 4, 5)
# o2 = Rectangle(4, 5)
# o3 = Circle(5)
# o_s = WorkWithShapes(o1, o2, o3)
# o_s.descriptions()
# o_s.perimeters()
# o_s.areas()

# Завдання 2 : Реалізація системи перевірки правил для класів за допомогою метакласів
# Опис завдання:
# Вам потрібно створити систему, яка забезпечує автоматичну перевірку, чи відповідають створені класи певним вимогам.
# Для цього потрібно використовувати метакласи.
# Вимоги до завдання:
# Створіть метаклас ValidationMeta:
# Перевіряйте, чи всі методи класу починаються зі слова do_ (наприклад, do_task, do_something_else).
# Перевіряйте, чи є в класі атрибут description, і чи є він рядком.
# Створіть базовий клас ValidatedClass:
# Визначте цей клас із використанням метакласу ValidationMeta.
# Створіть кілька класів, які наслідують ValidatedClass:
# Один клас повинен відповідати всім правилам.
# Інший клас має порушувати одне з правил (наприклад, методи не починаються з do_ або відсутній атрибут description).
# Додайте виключення:
# Якщо клас порушує правила метакласу, має бути викликана помилка ValueError із поясненням, що саме не відповідає вимогам.
# Реалізуйте програму, яка створює об'єкти цих класів:
# У програмі виведіть інформацію про те, чи успішно створено кожен клас, або ж, якщо є помилка, виведіть її текст.
# Додаткові вимоги:
# Використовуйте модуль abc для визначення базового класу.
# Додайте можливість автоматичного створення відсутнього атрибуту description з дефолтним значенням, якщо його немає.


class ValidationMeta(type):
    def __new__(cls, name, empty_tuple, args, **kwargs):
        print('-------------------------------------------------')
        print(f'Creating class {name} starts...')
        result_cls = super().__new__(cls, name, empty_tuple, args)
        if kwargs:
            for key, value in kwargs.items():
                setattr(result_cls, key, value)
        funks_names = [key for key, value in args.items() if 'function' in str(value)]
        funk_flag = True
        for x in funks_names:
            if x[:3] != 'do_':
                funk_flag = False
                raise Exception(f'Function {x} in {name} has incorrect name!')
        if funk_flag:
            print('All functions names starts with do_')
        if 'description' in args.keys():
            if type(args['description']) == str:
                print(f'Class {name} has attribute description and it is string')
            else:
                raise Exception(f'Class {name} has attribute description but it is not string')
        else:
            action = input(f'Class {name} has no attribute description. Add it? y/n ')
            if action == 'y':
                setattr(result_cls, 'description', 'Default description')
                print('Attribute description added as Default description')
            else:
                print('Attribute description is not added')
        print(f'Creating class {name} successful')
        print('-------------------------------------------------')
        return result_cls


try:
    class ValidatedClass1(metaclass=ValidationMeta):
        description = "2"

        def do_task(self):
            pass
except Exception as ex:
    print(ex)


try:
    class ValidatedClass2(metaclass=ValidationMeta):
        description = "2"

        def do_task(self):
            pass

        def not_do(self):
            pass
except Exception as ex:
    print(ex)


try:
    class ValidatedClass3(metaclass=ValidationMeta):
        description = 3

        def do_task(self):
            pass
except Exception as ex:
    print(ex)


try:
    class ValidatedClass4(metaclass=ValidationMeta):
        def do_task(self):
            pass
except Exception as ex:
    print(ex)
