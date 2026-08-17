def create_adjacency_list(edges):
    adj_list = {}

    for from_vertex, to_vertex in edges:
        if from_vertex not in adj_list:
            adj_list[from_vertex] = []
        if to_vertex not in adj_list:
            adj_list[to_vertex] = []
        adj_list[from_vertex].append(to_vertex)

    return adj_lis

def add_vertex_to_list(adj_list, vertex):
    if vertex not in adj_list:
        adj_list[vertex] = []
    return adj_list


def add_edge_to_list(adj_list, from_vertex, to_vertex):
    if from_vertex not in adj_list:
        adj_list[from_vertex] = []
    if to_vertex not in adj_list:
        adj_list[to_vertex] = []
    adj_list[from_vertex].append(to_vertex)
    return adj_list

def display_list(adj_list):
    for vertex, edges in adj_list.items():
        print(f"{vertex}: {edges}")

if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 2), (2, 0)]

    adj_list = create_adjacency_list(edges)
    print("список смежности:")
    display_list(adj_list)

    adj_list = add_vertex_to_list(adj_list, 3)
    print("после добавления вершины 3:")
    display_list(adj_list)

    adj_list = add_edge_to_list(adj_list, 1, 3)
    print("после добавления ребра (1 - 3):")
    display_list(adj_list)