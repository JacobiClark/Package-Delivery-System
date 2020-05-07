class HashTable(object):
    def __init__(self, buckets=10):
        # Initiate our array with empty values.
        self.array = [None] * buckets
    
    def hash_key(self, key):
        """Get the bucket of our array for a specific string key"""
        length = len(self.array)
        return hash(key) % length
        
    def insert_kvp(self, key, value):
        """Add a value to our array by its key"""
        bucket = self.hash_key(key)
        if self.array[bucket] is not None:
            for kvp in self.array[bucket]:
                # If key is found, then update
                # its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.array[bucket].append([key, value])
        else:
            self.array[bucket] = []
            self.array[bucket].append([key, value])
    
    def get_value(self, key):
        bucket = self.hash_key(key)
        for kvp in self.array[bucket]:
            if kvp[0] == key:
                return kvp[1]

    def remove_kvp(self, key, value):
        bucket = self.hash_key(key)
        for kvp in self.array[bucket]:
            if kvp[0] == key:
                return[kvp[1]]
                del kvp

