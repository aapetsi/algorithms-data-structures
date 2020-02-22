class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"Val: {self.val}, Next: {self.next}"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        if self.length == 0:
            return None
        current = self.head
        new_tail = self.head
        while current.next:
            new_tail = current
            current = current.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current

    def shift(self):
        if self.length == 0:
            return None
        current_head = self.head
        self.head = current_head.next
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current_head

    def unshift(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self
    
    def get(self, val):
        pass

    def __str__(self):
        return f"Head: {self.head}, Tail: {self.tail}"


linked_list = SinglyLinkedList()
linked_list.push("hello")
linked_list.push("world")
linked_list.push("bye bye")
linked_list.push("world")
linked_list.push("bye bye")
print(linked_list.length)
print(linked_list.unshift('apetsi'))
print(linked_list.unshift('ampiah'))
print(linked_list.length)
