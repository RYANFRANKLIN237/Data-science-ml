class Person:
    def __init__(self, id, name, email, age):
        self._id = id
        self._name = name
        self._email = email
        self._age = age

    # Getters
    def get_id(self): return self._id
    def get_name(self): return self._name
    def get_email(self): return self._email
    def get_age(self): return self._age

    # Setters
    def set_id(self, id): self._id = id
    def set_name(self, name): self._name = name
    def set_email(self, email): self._email = email
    def set_age(self, age): self._age = age

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Email: {self._email}, Age: {self._age}"

class Customer(Person):
    def __init__(self, id, name, email, age, balance, income):
        super().__init__(id, name, email, age)
        self._balance = balance
        self._income = income

    # Getters and Setters for balance and income
    def get_balance(self): return self._balance
    def set_balance(self, balance): self._balance = balance
    def get_income(self): return self._income
    def set_income(self, income): self._income = income

    def __str__(self):
        return f"{super().__str__()}, Balance: {self._balance}, Income: {self._income}"