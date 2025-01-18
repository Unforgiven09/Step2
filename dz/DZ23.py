# Завдання 1
# Створити клас Калькулятор. У класі має бути реалізовано наступну функціональність:
#  Додавання двох чисел;
#  Віднімання двох чисел;
#  множення двох чисел;
#  Розподіл двох чисел;
#  Максимум із двох чисел;
#  Мінімум із двох чисел;
#  Відсоток числа;
#  Зведення числа до ступеня.
# Протестуйте всі можливості створеного класу  за допомогою модульного тестування (unittest).
# Усі виняткові ситуації логіруйте (записуйте) до окремого файлу logs.log
# Приклад логування -
# logging.basicConfig(level=logging.WARNING, filename="logs.log", filemode='w',
#  format="We have some error: %(asctime)s : %(levelname)s : %(message)s")
# logging.error("Test str work")

class Calculator:
    @staticmethod
    def count(*args, **kwargs):
        actions = {'+', '-', '*', '/', 'min', 'max', '%', '**'}
        if len(args) != 2:
            raise Exception("Func need 2 args!")
        if len(kwargs) != 1:
            raise Exception("Func need only 1 kwarg!")
        if not set(kwargs.values()) & actions:
            raise Exception("Func need kwarg with value like '+', '-', '*', '/', 'min', 'max', '%', '**'!")
        else:
            if type(args[0]) and type(args[1]) != int or float:
                try:
                    args[0], args[1] = float(args[0]), float(args[1])
                except (ValueError, TypeError):
                    pass
            if set(kwargs.values()) == {'+'}:
                return args[0] + args[1]
            elif set(kwargs.values()) == {'-'}:
                return args[0] - args[1]
            elif set(kwargs.values()) == {'*'}:
                return args[0] * args[1]
            elif set(kwargs.values()) == {'/'}:
                if args[1] != 0:
                    return args[0] / args[1]
                else:
                    raise Exception('Division to ZERO alarm!')
            elif set(kwargs.values()) == {'min'}:
                return min(args[0], args[1])
            elif set(kwargs.values()) == {'max'}:
                return max(args[0], args[1])
            elif set(kwargs.values()) == {'%'}:
                return args[0] * args[1] / 100
            elif set(kwargs.values()) == {'**'}:
                return args[0] ** args[1]


# Додатково - Завдання 2: Тестування функції для обчислення факторіалу
# Створіть функцію factorial(n), яка приймає позитивне ціле число n як аргумент і повертає його факторіал.
# Факторіал числа n – це добуток всіх позитивних цілих чисел від 1 до n.
# Напишіть юніт-тести для функції factorial, використовуючи модуль unittest. Ваші тести повинні включати такі випадки:
# Позитивний тест: Перевірте, чи функція правильно обчислює факторіал для заданого числа (наприклад, 5! = 120).
# Тест на нуль: Перевірте, чи факторіал числа 0 дорівнює 1.
# Тест на негативне число: Перевірте, що функція генерує виключення ValueError, якщо аргумент є негативним.
# Тест на неціле число: Перевірте, що функція генерує виключення ValueError, якщо аргумент не є цілим числом.
# Створіть файл test_factorial.py, в якому визначте клас для тестування функцій factorial.
# Запустіть тести, використовуючи модуль unittest.


def factorial(n):
    if type(n) != int:
        raise ValueError('Use int nums only')
    elif n < 0:
        raise ValueError('Use positive nums only')
    return n * factorial(n-1) if n > 0 else 1
