from abc import ABC, abstractmethod
import copy


class ConsoleManager:
    __instance =None

    @staticmethod
    def getInstance():
        if ConsoleManager.__instance is None:
            ConsoleManager()
        return ConsoleManager.__instance

    def __init__(self):
        if ConsoleManager.__instance is not None:
            raise Exception('Only 1')
        else:
            ConsoleManager.__instance = self

    def log(self, massage):
        print('Log entry:', massage)


log_manager = ConsoleManager.getInstance()
log_manager.log('Singleton pattern in action')


class CarFactory:
    def create_car(self, type):
        if type == 'sedan':
            return Sedan()
        elif type == 'suv':
            return Suv()
        else:
            raise Exception("Error type!")


class Sedan:
    def sedan(self):
        print('new sedan')


class Suv:
    def suv(self):
        print('new suv')


car_factory = CarFactory()
client1 = car_factory.create_car('sedan')
client1.sedan()


class ReportBuilder:
    def __init__(self):
        self.report = {'title': '', 'date': '', 'content': ''}

    def set_title(self, title):
        self.report['title'] = title

    def set_date(self, date):
        self.report['date'] = date

    def set_content(self, content):
        self.report['content'] = content

    def build(self):
        return self.report


builder = ReportBuilder()
builder.set_title('rep 1')
builder.set_date('20.01.2025')
builder.set_content('First report')
report = builder.build()

print(report)


class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class LightThemeFactory(UIFactory):
    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightCheckbox()


class DarkThemeFactory(UIFactory):
    def create_button(self):
        return DarkButton()

    def create_checkbox(self):
        return DarkCheckbox()


class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def click(self):
        pass


class LightButton(Button):
    def click(self):
        print('Light Theme button click')


class LightCheckbox(Button):
    def click(self):
        print('Light Theme checkbox click')


class DarkButton(Button):
    def click(self):
        print('Dark Theme button click')


class DarkCheckbox(Button):
    def click(self):
        print('Dark Theme checkbox click')


def client_code(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.click()
    checkbox.click()


light_factory = LightThemeFactory()
client_code(light_factory)
dark_factory = DarkThemeFactory()
client_code(dark_factory)


class Car:
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour

    def clone(self):
        return copy.copy(self)


prototype_car = Car('tesla', 'black')
cloned_car = prototype_car.clone()

print(vars(prototype_car))
print(vars(cloned_car))