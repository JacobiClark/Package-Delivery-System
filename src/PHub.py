import csv
import Truck
from Model import Graph, Location, Package, Truck
from datetime import timedelta
from HashTable import HashTable
import collections
# Hub class
 
class PHub:
    def start(self):
        priority_packages_hash_table = HashTable(50)
        packages_hash_table = HashTable(50)
        loading_dock = []
        graph = Graph()
        current_time = timedelta(hours=8)
        def load_package(package):
            loading_dock.append(package)
        
        #Reads Packages CSV file and instantiates a new package for each row
        #if package delivery by is end of day, package is appended to the regular package hash table
        #if package has an early delivery time, package is appended in to the priority package table.
        with open('../assets/csv/packages.csv') as csvfile:
            packages = csv.reader(csvfile)
            for data_row in packages:
                new_package = Package(*data_row)
                if new_package.deliver_by == 'EOD':
                    packages_hash_table.insert_kvp(new_package.package_ID, new_package)
                else:
                    priority_packages_hash_table.insert_kvp(new_package.package_ID, new_package)

        #Reads Locations CSV file and instantiates a Location object which is then added to the Graph's adjacency list and the location list
        with open('../assets/csv/locations.csv') as csvfile:
            locations = csv.reader(csvfile)
            for data_row in locations:
                new_location = Location(*data_row)
                graph.locations_hash_table.insert_kvp(new_location.location_ID, new_location)

        #Reads Distance CSV and adds a distance set to the distances list, creating in essence a 2D array.
        with open('../assets/csv/distances.csv') as csvfile:
            distances = csv.reader(csvfile)
            for data_row in distances:
                graph.distances_list.append(data_row)

        for s, distance_set in enumerate(graph.distances_list):
            for d, distance in enumerate(distance_set):
                graph.locations_hash_table.get_value(s).add_adjacent_path(d, distance) #graph.locations_hash_table.get_value(d)

        while len(loading_dock) < Truck.max_packages:
            if priority_packages_hash_table.item_count() != 0:
                for bucket in priority_packages_hash_table.table:
                    if bucket != None:
                        for kvp in bucket:
                            if len(loading_dock) < Truck.max_packages:
                                load_package(kvp[0])
                                bucket.remove(kvp)
            if packages_hash_table.item_count() != 0:
                for bucket in packages_hash_table.table:
                    if bucket != None:
                        for kvp in bucket:
                            if len(loading_dock) < Truck.max_packages:
                                load_package(kvp[0])
                                bucket.remove(kvp)
        
        Truck2 = Truck(2, graph.locations_hash_table.get_value(0))

        #LOAD THE TRUCK
        while Truck2.has_room():
            for package in loading_dock:
                Truck2.load_package(package)
                loading_dock.remove(package)
        graph.sort_packages(Truck2.delivery_list,graph.locations_hash_table.get_value(0))
        print(Truck2.delivery_list)
        start_location = graph.locations_hash_table.get_value(0).location_ID
        print(graph.locations_hash_table.get_value(0).adjacent_paths[1])
        print(graph.calculate_distance(graph.locations_hash_table.get_value(0),2))

        #Truck2.deliver_packages()

        #while len(Truck2.delivery_list) < Truck2.max_packages:

        #LOAD PACKAGES TO LOADING DOCK
        
phub = PHub()
phub.start()



