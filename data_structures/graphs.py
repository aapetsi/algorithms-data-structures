class Graph:
    """
    Implementation of an unidrected graph
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.adjacency_list and v2 in self.adjacency_list:
            self.adjacency_list[v1].append(v2)
            self.adjacency_list[v2]. append(v1
        else:
            raise KeyError('Key not found in adjacency list')

    def remove_edge(self, v1, v2):
        self.adjacency_list[v1].remove(v2)
        self.adjacency_list[v2].remove(v1)

    def remove_vertex(self, v):
        del self.adjacency_list[v]
        for key in self.adjacency_list:
            if v in self.adjacency_list[key]:
                self.adjacency_list[key].remove(v)
    
    def __repr__(self):
        s = ''
        for key in self.adjacency_list:
            s += f'{key}: {self.adjacency_list[key]}\n'
        return s

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def dfs_recursive(self, start):
        result = []
        visited = {}

        def dfs(start):
            if not start:
                return
            visited[start] = True
            result.append(start)
            neighbors = self.get_neighbors(start)
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)

        return result

    def bfs(self, start, end):
        pass


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')

print(g.adjacency_list)
print(g.dfs_recursive('A'))
