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
            # This bucket already contain some values.
            # This means that this add MIGHT be an update
            # to a key that already exist. Instead of just storing
            # the value we have to first look if the key exist.
            for kvp in self.array[bucket]:
                # If key is found, then update
                # its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                # If no breaks was hit in the for loop, it 
                # means that no existing key was found, 
                # so we can simply just add it to the end.
                self.array[bucket].append([key, value])
        else:
            # This bucket is empty. We should initiate 
            # a list and append our key-value-pair to it.
            self.array[bucket] = []
            self.array[bucket].append([key, value])
    
    def get_kvp(self, key):
        """Get a value by key"""
        bucket = self.hash_key(key)
        if self.array[bucket] is None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does 
            # then return its value.
            for kvp in self.array[bucket]:
                if kvp[0] == key:
                    return kvp[1]
            
            # If no return was done during loop,
            # it means key didn't exist.
            raise KeyError()
