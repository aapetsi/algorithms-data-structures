class HashTable:
    def __init__(self, size=53):
        self.storage = [None] * size

    def _hash(self, key):
        total = 0
        prime = 3
        for ch in key:
            val = ord(ch) - 96
            total = (total * prime + val) % len(self.storage)

        return total

    def insert(self, key, value):
        index = self._hash(key)
        if self.storage[index] is None:
            self.storage[index] = [[key, value]]
        else:
            self.storage[index].append([key, value])

    def retrieve(self, key):
        index = self._hash(key)
        val = self.storage[index]
        if val is None:
            return None
        for item in val:
            if item[0] == key:
                return item[1]

    def keys(self):
        all_keys = set()
        for item in self.storage:
            if item is not None:
                for val in item:
                    all_keys.add(val[0])
        return all_keys

    def values(self):
        all_values = set()
        for item in self.storage:
            if item is not None:
                for val in item:
                    all_values.add(val[1])
        return all_values
