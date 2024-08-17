# vehicles.py

class Vehicle:
    def __init__(self, model, make, year, price):
        self._model = model
        self._make = make
        self._year = year
        self._price = price
        self._discount = 0

    def get_model(self):
        return self._model

    def get_make(self):
        return self._make

    def get_year(self):
        return self._year

    def get_price(self):
        return self._price

    def get_discount(self):
        return self._discount

    def set_discount(self, discount):
        self._discount = discount

    def display(self):
        print(f"Model: {self._model}, Make: {self._make}, Year: {self._year}, Price: {self._price}, Discount: {self._discount}%")