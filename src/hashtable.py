#JACOB CLARK 001190089
class HashTable():
    #Initializes a hash table with 10 buckets as default or however may buckets were passed in as paramaters
    #Time Complexity: O(1)
    def __init__(self, buckets=10):
        self.table = [None] * buckets
    
    #Returns a key's hash value using python's hash function and modding it by the length of the table
    #Time Complexity: O(1)
    def hash_key(self, key):
        """Get the bucket of our table for a specific string key"""
        length = len(self.table)
        return hash(key) % length
    
    #inserts a KVP into the hash table. The key is first hashed and inserted if bucket is empty, if not, it appends the kvp to the bucket, or updates
    #if the key already exists
    #Time Complexity: O(n)    
    def insert_kvp(self, key, value):
        """Add a value to our table by its key"""
        bucket = self.hash_key(key)
        if self.table[bucket] is not None:
            for kvp in self.table[bucket]:
                # If key is found, then update
                # its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.table[bucket].append([key, value])
        else:
            self.table[bucket] = []
            self.table[bucket].append([key, value])
    
    #Takes a key as a paramater, and if key is in its hashed bucket, returns the value.
    #Time Complexity: O(n) 
    def get_value(self, key):
        bucket = self.hash_key(key)
        for kvp in self.table[bucket]:
            if kvp[0] == key:
                return kvp[1]
    #Iterates through the hash table and returns all kvps
    #Time Complexity: O(n)
    def get_all_values(self):
        values_list = []
        for bucket in self.table:
            if bucket != None:
                for kvp in bucket:
                    values_list.append(kvp[1])
        return values_list
    #Iterates through the hash table and returns all kvps where package status is 'At Hub'
    #Time Complexity: O(n)
    def get_packages_in_hub(self):
        values_list = []
        for bucket in self.table:
            if bucket != None:
                for kvp in bucket:
                    if kvp[1].status == 'At Hub':
                        values_list.append(kvp[1])
        return values_list

    #Iterates through the hash table and returns number of items in the hash table
    #Time Complexity: O(n)
    def item_count(self):
        count = 0
        for bucket in self.table:
            if bucket != None or []:
                for kvp in bucket:
                    count += 1
        return count