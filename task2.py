from collections import deque
from task1 import DirectedGraph

def bfs(graph, start):
    if start not in graph.graph:
        return []

    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            for neighbor in graph.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

if __name__ == "__main__":
    g = DirectedGraph()

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")

    print("граф:")
    g.display()

    print("обход в ширину с вершины A:", bfs(g, "A"))