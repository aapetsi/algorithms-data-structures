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


g = Graph()
g.add_vertex("Tokyo")
g.add_vertex("Dallas")
g.add_vertex("Aspen")
g.add_vertex("Los Angeles")
g.add_vertex("Hong Kong")
g.add_edge("Tokyo", "Dallas")
g.add_edge("Aspen", "Dallas")
g.add_edge("Hong Kong", "Tokyo")
g.add_edge("Hong Kong", "Dallas")
g.add_edge("Los Angeles", "Hong Kong")
g.add_edge("Los Angeles", "Aspen")
g.remove_vertex("Hong Kong")
g.remove_vertex("Aspen")
print(g.adjacency_list)
