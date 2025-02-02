import pickle
import json
import os

# Завдання 1
# Маємо певний словник з назвами країн і столиць. Назва країни використовується як ключ, назва столиці — як значення.
# Реалізуйте: додавання, видалення, пошук, редагування, збереження та завантаження даних (використовуючи стиснення та
# розпакування).

countries = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Japan": "Tokyo",
    "Canada": "Ottawa",
    "Brazil": "Brasilia",
    "India": "New Delhi",
    "China": "Beijing",
    "Australia": "Canberra"
}


# реализуем функции сохранения и загрузки словаря, чтоб в дальнейшем при любом действии просто вызывать их.
def create_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_dir, file_name)


def save_countries(file_name, data):
    with open(create_path(file_name), 'wb') as file:
        pickle.dump(data, file)


def load_countries(file_name):
    with open(create_path(file_name), 'rb') as file:
        data = pickle.load(file)
    return data


# реализуем все действия из условия.
def show_all_countries(file_name):
    temp_countries_dict = load_countries(file_name)
    for x, y in temp_countries_dict.items():
        print(x, ":", y)


def add_country(file_name, new_country, new_capital):
    temp_countries_dict = load_countries(file_name)
    temp_countries_dict[new_country] = new_capital
    print(f'{new_country} added with capital {new_capital}')
    save_countries(file_name, temp_countries_dict)


def del_country(file_name, country_to_del):
    temp_countries_dict = load_countries(file_name)
    if temp_countries_dict[country_to_del]:
        temp_countries_dict.pop(country_to_del)
        print(f'{country_to_del} is deleted')
        save_countries(file_name, temp_countries_dict)
    else:
        raise Exception(f"{country_to_del} is not in file")


def find_country(file_name, country_to_find):
    temp_countries_dict = load_countries(file_name)
    return temp_countries_dict[country_to_find]


def change_country(file_name, country, new_capital):
    temp_countries_dict = load_countries(file_name)
    if temp_countries_dict[country]:
        temp_countries_dict[country] = new_capital
        save_countries(file_name, temp_countries_dict)
    else:
        raise Exception(f"{country} is not in file")


try:
    add_country('countries_dz27', 'Ukraine', 'Kyiv')
    del_country('countries_dz27', 'Italy')
    print(find_country('countries_dz27', 'India'))
    change_country('countries_dz27', 'India', 'Chicken Curry')
    show_all_countries('countries_dz27')
    del_country('countries_dz27', 'Mordor')
except Exception as ex:
    print(ex)


# Завдання 2
# Створіть клас «Літак». Наповніть його необхідними характеристиками та методами. Реалізуйте стиснення та розпакування
# об'єктів класу «Літак» з використанням модуля pickle.
# Додайте можливість стиснення/розпакування за допомогою модуля json.

class Airplane:
    def __init__(self, name, size, sits):
        self.name = name
        self.size = size
        self.sits = sits

    def __str__(self):
        return f'Name = {self.name}\nSize = {self.size}\nSits = {self.sits}'

    def to_dict(self):
        return {"name": self.name, "size": self.size, "sits": self.sits}

    @staticmethod
    def from_dict(dict_plane):
        return Airplane(dict_plane["name"], dict_plane["size"], dict_plane["sits"])


def serialize_p(obj):
    return pickle.dumps(obj)


def deserialize_p(obj):
    return pickle.loads(obj)


def serialize_json(obj):
    return json.dumps(obj.to_dict())


def deserialize_json(obj):
    temp = json.loads(obj)
    return Airplane.from_dict(temp)


ap1 = Airplane('boiling', 'large', 747)
ser_ap1 = serialize_p(ap1)
print(deserialize_p(ser_ap1))
ser_ap2 = serialize_json(ap1)
print(deserialize_json(ser_ap2))

# Додатково 3
# Ти розробляєш систему керування користувачами для веб-застосунку. Дані про користувачів зберігаються
# у файлі users.json. Кожен користувач має такі поля:
# id (унікальний ідентифікатор)
# name (ім'я)
# age (вік)
# email (електронна пошта)
# Зчитати JSON-файл users.json, який містить список користувачів.
# Додати нового користувача до списку. Новий користувач задається у вигляді словника:
# new_user = {"id": 4, "name": "Emma", "age": 28, "email": "emma@example.com"}
# Оновити вік користувача за його id. Наприклад, змінити вік користувача з id = 2 на 30.
# Зберегти оновлений список користувачів назад у users.json.
# [
#     {"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com"},
#     {"id": 2, "name": "Bob", "age": 22, "email": "bob@example.com"},
#     {"id": 3, "name": "Charlie", "age": 30, "email": "charlie@example.com"}
# ]
# Реалізуй функції:
# read_users(filename) – зчитує та повертає список користувачів.
# add_user(filename, new_user) – додає нового користувача.
# update_age(filename, user_id, new_age) – змінює вік користувача за id.
# save_users(filename, users) – зберігає зміни у JSON-файл.


class User:
    def __init__(self, id, name, age, email):
        self.id = id
        self.name = name
        self.age = age
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
        }

    @staticmethod
    def from_dict(dict):
        return User(dict["id"], dict["name"], dict["age"], dict["email"])

    def __str__(self):
        return f'user id {self.id}'


def read_users(file_name):
    with open(create_path(file_name), 'r') as file:
        data = json.load(file)
    return data


def save_users(file_name, data):
    with open(create_path(file_name), 'w') as file:
        json.dump(data, file, indent=4)


def add_user(file_name, obj_new_user):
    data = read_users(file_name)
    data.append(obj_new_user.to_dict())
    save_users(file_name, data)


def update_user(file_name, user_id_to_update, new_age):
    data = read_users(file_name)
    user_list = []
    data_new = []
    for x in data:
        user_list.append(User.from_dict(x))
    for x in user_list:
        if x.id == user_id_to_update:
            x.age = new_age
        data_new.append(x.to_dict())
    save_users(file_name, data_new)


new_user = {"id": 4, "name": "Emma", "age": 28, "email": "emma@example.com"}
add_user('users_dz27.json', User.from_dict(new_user))
update_user('users_dz27.json', 1, 30)
