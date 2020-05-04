from HashTable import HashTable
from Path import Path
import datetime

class Location():
    def __init__(self, location_ID, name, address, zip_code):
        self.location_ID = int(location_ID)
        self.name = name
        self.address = address
        self.zip_code = zip_code

    def get_location_ID(self):
        return int(self.location_ID)

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

    def get_package_id(self):
        return int(self.package_ID)

class Graph:
    def __init__(self):
        self.locations_list = []
        self.distances_list = []
        self.adjacency_list = {}
        
    def aadd_Path(self, from_location, to_location, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)
 