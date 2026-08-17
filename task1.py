class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.graph:
            self.add_vertex(from_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)
        self.graph[from_vertex].append(to_vertex)

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {edges}")

if __name__ == "__main__":
    g = DirectedGraph()

    g.add_vertex("A")
    g.add_vertex("B")

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")
    g.add_edge("C", "A")

    print("ориентированный граф:")
    g.display()