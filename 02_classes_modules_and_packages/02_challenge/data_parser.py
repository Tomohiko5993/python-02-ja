# data_parser.py

from vehicles import Vehicle

def parse_vehicle_data(file_path):
    vehicles = []
    with open(file_path, 'r') as file:
        for line in file:
            model, make, year, price = line.strip().split(',')
            vehicle = Vehicle(model, make, int(year), float(price))
            vehicles.append(vehicle)
    return vehicles