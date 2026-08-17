def create_adjacency_matrix(edges, num_vertices):
    matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for from_vertex, to_vertex in edges:
        matrix[from_vertex][to_vertex] = 1

    return matrix

def add_vertex_to_matrix(matrix):
    for row in matrix:
        row.append(0)
    matrix.append([0] * len(matrix[0]))
    return matrix

def add_edge_to_matrix(matrix, from_vertex, to_vertex):
    if from_vertex < len(matrix) and to_vertex < len(matrix):
        matrix[from_vertex][to_vertex] = 1
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 2), (2, 0)]
    num_vertices = 3

    matrix = create_adjacency_matrix(edges, num_vertices)
    print("матрица смежности:")
    display_matrix(matrix)

    matrix = add_vertex_to_matrix(matrix)
    print("после добавления вершины:")
    display_matrix(matrix)

    matrix = add_edge_to_matrix(matrix, 1, 3)
    print("после добавления ребра (1 - 3):")
    display_matrix(matrix)