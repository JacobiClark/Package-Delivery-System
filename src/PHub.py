import csv
#from Graph import Graph, Location, Package
import datetime
from HashTable import HashTable
import collections
# Hub class
class Location():
    def __init__(self, location_ID, name, address, zip_code):
        self.location_ID = location_ID
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
        self.distances_list = []
        self.locations_list = []
        self.adjacency_list = {}
        self.edge_weights = {}


    def add_location(self, location):
        self.adjacency_list[location] = {}
            
    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)
        
    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
 
class PHub:
    def start(self):
        packages_hash_table = HashTable(50)
        graph = Graph()

        with open('../assets/csv/packages.csv') as csvfile:
            packages = csv.reader(csvfile)
            for data_row in packages:
                new_package = Package(*data_row)
                packages_hash_table.insert_kvp(new_package.get_package_id(), new_package)

        with open('../assets/csv/locations.csv') as csvfile:
            locations = csv.reader(csvfile)
            for data_row in locations:
                new_location = Location(*data_row)
                graph.add_location(new_location)
                graph.locations_list.append(new_location)

        with open('../assets/csv/distances.csv') as csvfile:
            distances = csv.reader(csvfile)
            for data_row in distances:
                graph.distances_list.append(data_row)
            print(graph.distances_list)

        for location in graph.adjacency_list:
            for i, distance_set in enumerate(graph.distances_list):
                for j, edge in enumerate(distance_set):
                    if edge != '':
                        graph.adjacency_list[location][graph.locations_list[i]] = float(j)
                    else:
                        graph.adjacency_list[location][graph.locations_list[j]] = float(i)

        print(graph.adjacency_list[graph.locations_list[1]][graph.locations_list[1]])




        
phub = PHub()
phub.start()


