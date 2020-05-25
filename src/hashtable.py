
class HashTable(object):
    def __init__(self, buckets=10):
        # Initiate our table with empty values.
        self.table = [None] * buckets
    
    def hash_key(self, key):
        """Get the bucket of our table for a specific string key"""
        length = len(self.table)
        return hash(key) % length
        
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
    
    def get_value(self, key):
        bucket = self.hash_key(key)
        for kvp in self.table[bucket]:
            if kvp[0] == key:
                return kvp[1]
    
    def get_all_values(self):
        values_list = []
        for bucket in self.table:
            if bucket != None:
                for kvp in bucket:
                    values_list.append(kvp[1])
        return values_list

    def get_packages_in_hub(self):
        values_list = []
        for bucket in self.table:
            if bucket != None:
                for kvp in bucket:
                    if kvp[1].status == 'At Hub':
                        values_list.append(kvp[1])
        return values_list


    def remove_kvp(self, key):
        bucket = self.hash_key(key)
        for kvp in self.table[bucket]:
            if kvp[0] == key:
                self.table[bucket].remove(kvp)

    def item_count(self):
        count = 0
        for bucket in self.table:
            if bucket != None or []:
                for kvp in bucket:
                    count += 1
        return count