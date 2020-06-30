import csv
from Model import Graph, Location, Package, Truck
import datetime
from HashTable import HashTable
import collections
# Hub class
 
class PHub:
    def __init__(self):
        self.priority_packages_hash_table = HashTable(50)
        self.packages_hash_table = HashTable(50)
        self.late_packages_hash_table = HashTable(10)
        self.current_time = datetime.datetime(2020,3,15,8,0,0)
        self.package_count = 0
        self.loading_dock = []
        self.locations_list = []
        self.graph = Graph()

    def load_package(self, package):
        self.loading_dock.append(package)
        package.status = 'Loaded on Truck 2'
    
    def print_package_statuses(self, package_count, stop_time):
        self.package_count = package_count
        self.stop_time = stop_time
        if self.package_count > 0:
            print('Status of all packages at ' + str(self.stop_time))
        print('----------Late arrival package statuses----------')
        for package in self.late_packages_hash_table.get_all_values():
            print('Package #' + str(package.package_ID) + ' status: ' + package.status)
        print('----------Priority package statuses----------')
        for package in self.priority_packages_hash_table.get_all_values():
            print('Package #' + str(package.package_ID) + ' status: ' + package.status)
        print('----------Package statuses----------')        
        for package in self.packages_hash_table.get_all_values():
            print('Package #' + str(package.package_ID) + ' status: ' + package.status)
        


    
    def start(self, stop_time):
        self.stop_time = stop_time
        #Reads Packages CSV file and instantiates a new package for each row
        #if package delivery by is end of day, package is appended to the regular package hash table
        #if package has an early delivery time, package is appended in to the priority package table.
        with open('../assets/csv/packages.csv') as csvfile:
            packages = csv.reader(csvfile)
            for data_row in packages:
                new_package = Package(*data_row)
                if new_package.deliver_by == 'EOD' and 'Delayed on flight' not in new_package.package_notes:
                    self.packages_hash_table.insert_kvp(new_package.package_ID, new_package)
                    self.package_count += 1
                elif 'Delayed on flight' in new_package.package_notes:
                    self.late_packages_hash_table.insert_kvp(new_package.package_ID, new_package)
                    self.package_count += 1
                else:
                    self.priority_packages_hash_table.insert_kvp(new_package.package_ID, new_package)
                    self.package_count += 1

        #Reads Locations CSV file and instantiates a Location object which is then added to the Graph's adjacency list and the location list
        with open('../assets/csv/locations.csv') as csvfile:
            locations = csv.reader(csvfile)
            for data_row in locations:
                new_location = Location(*data_row)
                self.graph.locations_hash_table.insert_kvp(new_location.address, new_location)
                self.locations_list.append(new_location)
        #Reads Distance CSV and adds a distance set to the distances list, creating in essence a 2D array.
        with open('../assets/csv/distances.csv') as csvfile:
            distances = csv.reader(csvfile)
            for data_row in distances:                     
                self.graph.distances_list.append(data_row)

        for s, distance_set in enumerate(self.graph.distances_list):
            for d, distance in enumerate(distance_set):
                self.locations_list[s].add_adjacent_path(self.locations_list[d].address, distance)
        #MAIN SECTION, START LOADING HERE!!!
        #while self.package_count > 0:
        start_location = self.graph.locations_hash_table.get_value('Hub')
        Truck2 = Truck(2, start_location, self.current_time)
        

        #Appends packages to the loading dock starting with priority packages, then regular packages, and adds in late packages when they come.
        while self.package_count > 0 and self.current_time < self.stop_time:
            while len(self.late_packages_hash_table.get_packages_in_hub()) > 0 and len(self.loading_dock) < Truck.max_packages and self.current_time > datetime.datetime(2020,3,15,10,20,0) :  #
                if len(self.loading_dock) == 0:
                    closest_package = self.graph.get_closest_location(start_location, self.late_packages_hash_table.get_packages_in_hub())
                    self.load_package(closest_package)
                closest_package = self.graph.get_closest_location(self.loading_dock[-1], self.late_packages_hash_table.get_packages_in_hub())
                self.load_package(closest_package)
            while len(self.priority_packages_hash_table.get_packages_in_hub()) > 0 and len(self.loading_dock) < Truck.max_packages:  #
                if len(self.loading_dock) == 0:
                    closest_package = self.graph.get_closest_location(start_location, self.priority_packages_hash_table.get_packages_in_hub())
                    self.load_package(closest_package)
                closest_package = self.graph.get_closest_location(self.loading_dock[-1], self.priority_packages_hash_table.get_packages_in_hub())
                self.load_package(closest_package)
            while len(self.packages_hash_table.get_packages_in_hub()) > 0 and len(self.loading_dock) < Truck.max_packages:  #
                if len(self.loading_dock) == 0:
                    closest_package = self.graph.get_closest_location(start_location, self.packages_hash_table.get_packages_in_hub())
                    self.load_package(closest_package)
                closest_package = self.graph.get_closest_location(self.loading_dock[-1], self.packages_hash_table.get_packages_in_hub())
                self.load_package(closest_package)

            #LOAD THE TRUCK
            while Truck2.has_room() and len(self.loading_dock) > 0:
                for package in self.loading_dock:
                    Truck2.load_package(package)
                    self.loading_dock.remove(package)

            #Sort packages on Truck's delivery list
            self.graph.sort_packages(Truck2, start_location)
            packages_delivered = len(Truck2.delivery_list)
            #Make requried adjustments to time and package count
            self.current_time = Truck2.deliver_packages(self.graph, self.current_time, self.stop_time)
            self.package_count -= packages_delivered
        #Prints statuses of all packages after program is finished running
        self.print_package_statuses(self.package_count, self.stop_time)
        #If all packages delivered, prints miles
        if self.package_count == 0:
            print('Packages deliverd in ' + str(Truck2.distance_driven) + ' miles!')
        

        




