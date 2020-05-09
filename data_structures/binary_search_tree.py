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

    def bfs(self):
        data = []
        queue = []
        node = self.root
        queue.append(node)
        while len(queue):
            node = queue.pop(0)
            data.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return data

    def dfs_preorder(self):
        data = []
        current = self.root

        def traverse(node):
            data.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(current)

        return data

    def dfs_postorder(self):
        data = []
        current = self.root

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            data.append(node.value)

        traverse(current)

        return data

    def dfs_inorder(self):
        data = []
        current = self.root

        def traverse(node):
            if node.left:
                traverse(node.left)

            data.append(node.value)

            if node.right:
                traverse(node.right)

        traverse(current)

        return data



