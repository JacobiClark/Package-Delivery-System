from HashTable import HashTable
import datetime

class Graph:
    def __init__(self):
        self.locations_hash_table = HashTable(25)
        self.distances_list = []

    def add_location(self, new_location):
        self.locations_hash_table.insert_kvp(new_location.location_ID, new_location)

    def add_path(self, from_location, to_location, distance = 1.0):
        self.locations_hash_table.get_value(from_location).add_adjacent_path(self.locations_hash_table.get_value(to_location), distance)

    def calculate_distance(self, from_location, to_location):
        return float(self.locations_hash_table.get_value(from_location.address).adjacent_paths[to_location.address])

    def sort_packages(self, Truck, start_location_object):
        sorted_list = []
        current_location = start_location_object
        while len(Truck.delivery_list) !=  0:
            closest_package = Truck.delivery_list[0]
            for package in Truck.delivery_list:
                if self.calculate_distance(current_location, package) < self.calculate_distance(current_location, closest_package):
                    closest_package = package
            sorted_list.append(closest_package)
            current_location = self.locations_hash_table.get_value(closest_package.address)
            Truck.delivery_list.remove(closest_package)
        Truck.delivery_list = sorted_list




class Location():
    def __init__(self, location_ID, name, address, zip_code):
        self.adjacent_paths = {}
        self.location_ID = int(location_ID)
        self.name = name
        self.address = address
        self.zip_code = zip_code

    def add_adjacent_path(self, to_location, distance = 0):
        self.adjacent_paths[to_location] = distance


class Package:
    def __init__(self, package_ID, address, city, state, zip_code, deliver_by, weight_in_kilograms, package_notes):
        self.package_ID = int(package_ID)
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        if 'EOD' in deliver_by:
            self.deliver_by = "EOD"
        else: self.deliver_by = datetime.datetime.strptime(deliver_by, '%H:%M').time()
        self.weight_in_kilograms = weight_in_kilograms
        self.deliver_by = deliver_by
        self.package_notes = package_notes

class Truck:
    max_packages = 16
   
    def __init__(self, truck_number, start_location):
        self.max_packages = 16
        self.avg_speed_MPH = 18
        self.start_time = datetime.time(8, 00, 00)
        self.truck_number = truck_number
        self.start_location = start_location
        self.distance_driven = float(0)
        self.delivery_list = []

    def load_package(self, package):
        if len(self.delivery_list) < self.max_packages:
            self.delivery_list.append(package)

    def has_packages(self):
        return len(self.delivery_list) > 0

    def deliver_packages(self, Graph, start_time):
        current_location = self.start_location
        print('current mileage')
        print(self.distance_driven)
        while self.has_packages():
            self.distance_driven += Graph.calculate_distance(current_location, self.delivery_list[0])
            current_location = self.delivery_list.pop()
        print('distance driven')
        print(self.distance_driven)


    def has_room(self):
        return len(self.delivery_list) < self.max_packages