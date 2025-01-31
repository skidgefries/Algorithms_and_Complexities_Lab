import itertools
import time


def is_clique(graph, vertices):
    """Checks if a given set of vertices forms a clique in the graph."""
    for u in vertices:
        for v in vertices:
            if u != v and graph[u][v] == 0:  # Check for missing edge
                return False
    return True


def find_max_clique_brute_force(graph):
    """Finds the maximum clique using brute force."""
    num_vertices = len(graph)
    max_clique = []


    for i in range(1, 1 << num_vertices):  # Iterate through all subsets (2^n)
        subset = []
        for j in range(num_vertices):
            if (i >> j) & 1:  # Check if j-th bit is set
                subset.append(j)


        if is_clique(graph, subset):
            if len(subset) > len(max_clique):
                max_clique = subset


    return max_clique




def generate_random_graph(num_vertices, probability):
    """Generates a random undirected graph."""
    graph = [[0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):  # Avoid self-loops and double edges
            if random.random() < probability:
                graph[i][j] = 1
                graph[j][i] = 1  # Undirected graph
    return graph




def main():
    
    num_vertices = int(input('Enter the number of vertices: ')) # Example: Adjust as needed
    graph = generate_random_graph(num_vertices, 0.5) # Adjust probability as needed


    print("Graph (Adjacency Matrix):")
    for row in graph:
        print(row)


    start_time = time.time()
    max_clique = find_max_clique_brute_force(graph)
    end_time = time.time()


    print("\nMaximum Clique:", max_clique)
    print(f"Computation Time: {end_time - start_time:.4f} seconds")




if __name__ == "__main__":
    import random
    main()
