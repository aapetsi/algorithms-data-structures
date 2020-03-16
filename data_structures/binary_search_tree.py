class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return self

        current = self.root
        while True:
            if value == current.value:
                return None
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return self

                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return self
                current = current.right

    def find(self, value):
        if self.root is None:
            return False
        current = self.root
        found = False
        while not found and current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                found = True
        if not found:
            return False
        return current
    
    def contains(self, value):
        if self.root is None:
            return False
        current = self.root
        found = False
        while not found and current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False


tree = BinarySearchTree()
# print(tree.find(1))
tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(11)
tree.insert(2)
tree.insert(16)
tree.insert(7)
print(tree.find(10))
print(tree.contains(10))
# print(tree.root.right.value)