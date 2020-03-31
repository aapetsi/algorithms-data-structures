class HashTable:
    def __init__(self, size = 53):
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
        for item in val:
            if item[0] == key:
                print(item)
                return item
        return None


ht = HashTable()
ht.insert('ice-cream', 44.5)
ht.retrieve('ice-cream')
# print(ht.storage)
