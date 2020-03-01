class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None
        self.prev = None

    def __str__(self):
        return f"Val: {self.val}, Next: {self.nxt}, Prev: {self.prev}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nxt = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        if self.length == 0:
            return None

        removed_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = removed_node.prev
            self.tail.nxt = None
            removed_node.prev = None
        self.length -= 1
        return removed_node

    def print_list(self):
        arr = []
        current = self.head
        for x in range(self.length):
            obj = {
                "val": current.val,
                "next": current.nxt,
                "prev": current.prev}
            arr.append(obj)
            current = current.nxt
        print(arr)
