from hashtable imoprt HashTable

class Graph:
    def __init__(self):
        self.adjacency_list = {}
  
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []