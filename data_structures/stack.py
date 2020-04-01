class Stack:
    def __init__(self):
        self.storage = []
        self.size = 0

    def push(self, val):
        self.storage.append(val)
        self.size += 1

    def pop(self):
        self.storage.pop()
        self.size -= 1

    def get_size(self):
        return self.size
