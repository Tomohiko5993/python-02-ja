# ここにコードを書いてください
from abc import ABC, abstractmethod
# 抽象クラス Vehicle
class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def get_details(self):
        pass

# Car クラス
class Car(Vehicle):
    def get_details(self):
        return f"Car: {self.year} {self.make} {self.model}"

# Truck クラス
class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_details(self):
        return f"Truck: {self.year} {self.make} {self.model}, Towing Capacity: {self.towing_capacity}"

# 車両の詳細を取得する関数
def get_vehicle_details(vehicle):
    # ここにコードを書いてください
    #pass
    return vehicle.get_details()

# Example usage:
if __name__ == "__main__":
    car = Car(make="Toyota", model="Corolla", year=2021)
    truck = Truck(make="Ford", model="F-150", year=2020, towing_capacity=5000)

    print(get_vehicle_details(car))  # Car: 2021 Toyota Corolla
    print(get_vehicle_details(truck))  # Truck: 2020 Ford F-150, Towing Capacity: 5000