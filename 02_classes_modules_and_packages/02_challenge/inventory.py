# inventory.py

import re
from vehicles import Vehicle

class Inventory:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def apply_discount(self, condition, discount_rate):
        for vehicle in self.vehicles:
            if condition(vehicle):
                vehicle.set_discount(discount_rate)
                vehicle._price *= (1 - discount_rate / 100)

    def search_vehicles(self, pattern):
        regex = re.compile(pattern, re.IGNORECASE)
        return [vehicle for vehicle in self.vehicles if regex.search(vehicle.get_model())]

    def retrieve_vehicles(self):
        for vehicle in self.vehicles:
            yield vehicle