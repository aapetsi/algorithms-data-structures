class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        self.adjacency_list[v1].remove(v2)
        self.adjacency_list[v2].remove(v1)

    def remove_vertex(self, vertex):
        del self.adjacency_list[vertex]
        for key in self.adjacency_list:
            items = self.adjacency_list[key]
            if vertex in items:
                items.remove(vertex)

    def dfs_recursive(self, start):
        result = []
        visited = {}

        def dfs(vertex):
            if not vertex:
                return None
            visited[vertex] = True
            result.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    return dfs(neighbor)

        dfs(start)
        return result


g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")
print(g.dfs_recursive("B"))
# g.add_vertex("Tokyo")
# g.add_vertex("Dallas")
# g.add_vertex("Aspen")
# g.add_vertex("Los Angeles")
# g.add_vertex("Hong Kong")
# g.add_edge("Tokyo", "Dallas")
# g.add_edge("Aspen", "Dallas")
# g.add_edge("Hong Kong", "Tokyo")
# g.add_edge("Hong Kong", "Dallas")
# g.add_edge("Los Angeles", "Hong Kong")
# g.add_edge("Los Angeles", "Aspen")
# g.remove_vertex("Hong Kong")
# g.remove_vertex("Aspen")
# print(g.adjacency_list)
