
# Utilized Tepe (Let's Go Hashing) and Zybooks as a general outline
# for this class
class HashTable:

    # Initializes hash table
    def __init__(self, size=10):
        self.table = []
        for i in range(size):
            self.table.append([])

    # Creates a hash key = 0(1)
    def _get_hash(self, key):
        bucket = hash(key) % len(self.table)
        return bucket

    # Adds a new package to the hash table = O(n)
    def add(self, key, item):
        key_hash = self._get_hash(key)
        value = [key, item]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([value])
            return True
        else:
            for v in self.table[key_hash]:
                if v[0] == key:
                    v[1] = value
                    return True
            self.table[key_hash].append(value)
            return True

    # Retrieves a package from the hash table = 0(n)
    def get(self, key):
        key_hash = self._get_hash(key)

        if self.table[key_hash] is not None:
            for v in self.table[key_hash]:
                if v[0] == key:
                    return v[1]

        return None

    # Updates a package in the hash table = 0(n)
    def update(self, key, value):
        key_hash = self._get_hash(key)
        if self.table[key_hash] is not None:
            for v in self.table[key_hash]:
                if v[0] == key:
                    v[1] = value
                    print(v[1])
                    return True

    # Removes package from the hash table = 0(n)
    def remove(self, key):
        key_hash = self._get_hash(key)
        value = self.table[key_hash]

        for v in value:
            if v[0] == key:
                 value.remove([v[0], v[1]])


