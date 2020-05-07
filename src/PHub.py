import csv
import Truck
#from Graph import Graph, Location, Package
import datetime
from HashTable import HashTable
import collections
# Hub class
class Location():
    def __init__(self, location_ID, name, address, zip_code):
        self.adjacent_paths = {}
        self.location_ID = location_ID
        self.name = name
        self.address = address
        self.zip_code = zip_code

    def add_adjacent_path(self, to_location, distance = 0):
        self.adjacent_paths[to_location] = distance

    def print_adjacent_paths(self):
        print(self.adjacent_paths)


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


class Graph:
    def __init__(self):
        self.distances_list = []
        self.locations_list = []
        self.adjacency_list = {}
        self.edge_weights = {}
    
    def calculate_distance(self, from_address, to_location):
        for distance in self.locations_list:
            if distance.address == from_address:
                return distance.adjacent_paths[to_location]


    def add_location(self, location):
        self.adjacency_list[location.address] = {location}
 
class PHub:
    def start(self):
        priority_packages_hash_table = HashTable(50)
        packages_hash_table = HashTable(50)
        testlist = []
        graph = Graph()
            #Reads Packages CSV file and instantiates a new package for each row
            #if package delivery by is end of day, package is appended to the regular package hash table
            #if package has an early delivery time, package is appended in to the priority package table.
        with open('../assets/csv/packages.csv') as csvfile:
            packages = csv.reader(csvfile)
            for data_row in packages:
                new_package = Package(*data_row)
                if new_package.deliver_by == 'EOD':
                    packages_hash_table.insert_kvp(new_package.address, new_package)
                else:
                    priority_packages_hash_table.insert_kvp(new_package.address, new_package)
                
        #Reads Locations CSV file and instantiates a Location object which is then added to the Graph's adjacency list and the location list
        with open('../assets/csv/locations.csv') as csvfile:
            locations = csv.reader(csvfile)
            for data_row in locations:
                new_location = Location(*data_row)
                graph.add_location(new_location)
                graph.locations_list.append(new_location)

        #Reads Distance CSV and adds a distance set to the distances list, creating in essence a 2D array.
        with open('../assets/csv/distances.csv') as csvfile:
            distances = csv.reader(csvfile)
            for data_row in distances:
                graph.distances_list.append(data_row)

        #Uses the distance list to add the distance to every other location to every Location's adjacent path dictionary.
        for s, distance_set in enumerate(graph.distances_list):
            for d, distance in enumerate(distance_set):
                graph.locations_list[s].add_adjacent_path(graph.locations_list[d].address, graph.distances_list[s][d])
        
        Truck1 = Truck.Truck(1, graph.locations_list[0])
        #while len(Truck1.delivery_list) < Truck1.max_packages:

        #LOAD THE TRUCK
        current_location = graph.locations_list[0]
        for i,kvp in enumerate(priority_packages_hash_table.array):
            if kvp != None:
                print(current_location.address)
                print(graph.calculate_distance(current_location.address, kvp[0][1].address))


#        for i, kvp in enumerate(priority_packages_hash_table.array):
#            if kvp != None:
#                nearest_address = kvp[0][1]
#                print('hi')
#                print(current_location.address)
#                print(graph.calculate_distance(current_location.address, kvp[0][1].address))
#                if graph.calculate_distance(current_location.address, kvp[i][1].address) <= graph.calculate_distance(current_location.from_address, nearest_address):
#                    nearest_address = kvp[i-1][1]
#                    print(nearest_address)



        
phub = PHub()
phub.start()


