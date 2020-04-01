class Queue:
    def __init__(self):
        self.storage = []
        self.size = 0

    def enqueue(self, val):
        self.storage.append(val)
        self.size += 1

    def dequeue(self):
        self.storage.pop(0)
        self.size -= 1

    def get_size(self):
        return self.size
