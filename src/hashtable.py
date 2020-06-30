#JACOB CLARK 001190089
class HashTable():
    def __init__(self, buckets=10):
        # Initiate table with empty buckets
        self.table = [None] * buckets
    #Get bucket for a key
    def hash_key(self, key):
        length = len(self.table)
        return hash(key) % length
    #Add a KVP into table
    def insert_kvp(self, key, value):
        bucket = self.hash_key(key)
        if self.table[bucket] is not None:
            for kvp in self.table[bucket]:
                #Update Key if already in table
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.table[bucket].append([key, value])
        else:
            self.table[bucket] = []
            self.table[bucket].append([key, value])
    #Get value of key passed in    
    def get_value(self, key):
        bucket = self.hash_key(key)
        for kvp in self.table[bucket]:
            if kvp[0] == key:
                return kvp[1]
    #Get values of all KVPs in table
    def get_all_values(self):
        values_list = []
        for bucket in self.table:
            if bucket != None:
                for kvp in bucket:
                    values_list.append(kvp[1])
        return values_list
    #Return a list of al packages in hub
    def get_packages_in_hub(self):
        values_list = []
        for bucket in self.table:
            if bucket != None:
                for kvp in bucket:
                    if kvp[1].status == 'At Hub':
                        values_list.append(kvp[1])
        return values_list
    #Remove KVP that correlates with passed in key
    def remove_kvp(self, key):
        bucket = self.hash_key(key)
        for kvp in self.table[bucket]:
            if kvp[0] == key:
                self.table[bucket].remove(kvp)
    #Return count of items in table
    def item_count(self):
        count = 0
        for bucket in self.table:
            if bucket != None or []:
                for kvp in bucket:
                    count += 1
        return count
