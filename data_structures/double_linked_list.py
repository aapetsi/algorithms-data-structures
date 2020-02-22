class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, head, tail):
        self.head = None
        self.tail = None
        self.length = 0