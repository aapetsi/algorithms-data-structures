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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        count = 0
        current = self.head
        while count != index:
            current = current.next
            count += 1
        return current

    def set_node(self, index, val):
        found_node = self.get(index)
        if found_node is None:
            return False
        found_node.val = val
        return True

    def insert(self, index, val):
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            self.push(val)
            return True
        if index == 0:
            self.unshift(val)
            return True
        new_node = Node(val)
        previous = self.get(index - 1)
        temp = previous.next
        previous.next = new_node
        new_node.next = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.shift()
        previous = self.get(index - 1)
        removed = previous.next
        previous.next = removed.next
        self.length -= 1
        return removed

    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        previous = None
        next_item = None
        for i in range(self.length):
            next_item = node.next
            node.next = previous
            previous = node
            node = next_item
        return self

    def print_list(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.val)
            current = current.next
        print(arr)

    def __str__(self):
        current = self.head
        items = ''
        while current:
            if current.next is None:
                val = str(current.val)
                items += f'{val}'
            else: 
                val = str(current.val)
                items += f'{val} -> '
            

            current = current.next
        
        return items

ll = SinglyLinkedList()
ll.push(44)
ll.push(42)
ll.push(421)
ll.push(122)
ll.pop()
print(ll)