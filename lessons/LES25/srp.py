class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self._age = age

    # Getter for the age attribute.
    @property
    def age(self):
        return self._age

    # Setter for the age attribute, also validates the age is in a valid range.
    @age.setter
    def age(self, age):
        if age < 0 or age >= 130:
            raise ValueError("Age must be between 0 and 130 ")
        self._age = age


class Console:
    # Displays user information to the console.
    @staticmethod
    def display(obj):
        print(f"{obj.name} {obj.last_name} {obj._age}")

    # Reads user input from the console to create or update a User object.
    @staticmethod
    def input():
        name = input("Input name:")
        last_name = input("Input last name:")
        age = int(input("Input age:"))
        return User(name, last_name, age)


# Create a User object, display its information,
# update it with user input, then display it again.
obj = User("Bill", "Windows", 34)
Console.display(obj)
obj = Console.input()
Console.display(obj)
