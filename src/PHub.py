import csv
import Truck
import Model
import datetime
from HashTable import HashTable
import collections
# Hub class

class Graph:
    def __init__(self):
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

        #Reads Distance CSV and adds a distance set to the distances list, creating in essence a 2D array.
        with open('../assets/csv/distances.csv') as csvfile:
            distances = csv.reader(csvfile)
            for data_row in distances:
                graph.distances_list.append(data_row)

        #Uses the distance list to add the distance to every other location to every Location's adjacent path dictionary.
        for s, distance_set in enumerate(graph.distances_list):
            for d, distance in enumerate(distance_set):
                graph.locations_list[s].add_adjacent_path(graph.locations_list[d].address, graph.distances_list[s][d])
        
        Truck1 = Truck.Truck(1, 'Hub')


        #while len(Truck1.delivery_list) < Truck1.max_packages:

        #LOAD PACKAGES TO LOADING DOCK
        loading_dock = []
        current_location = graph.locations_list[0]
        for bucket in priority_packages_hash_table.array:
            closest_package = 1000
            closest_package = graph.locations_list[1]
            print(closest_package)
            if bucket != None:
                for kvp in bucket:
                    print(kvp[1].address)



#        for i, kvp in enumerate(priority_packages_hash_table.array):
#            if kvp != None:
#                nearest_address = kvp[0][1]
#                print('hi')
#                print(current_location.address)
#                print(graph.calculate_distance(current_location.address, kvp[0][1].address))
#                if graph.calculate_distance(current_location.address, kvp[i][1].address) <= graph.calculate_distance(current_location.from_address, nearest_address):
#                    nearest_address = kvp[i-1][1]
#                    print(nearest_address)for kvp in self.array[bucket]:
#            if kvp[0] == key:
 #               return[kvp[1]]
  #              del kvp



        
phub = PHub()
phub.start()


