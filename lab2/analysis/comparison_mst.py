import matplotlib.pyplot as plt
import time
import random
import sys
sys.path.append("lab2")
from algorithms.kruskals import kruskal
from algorithms.prims import prims

sys.path.append("util")
from plot_inputVstime import plot_graph2

# Function to generate random adjacency matrix
def generate_graph(num_vertices, density=0.5, max_weight=10):
    graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < density:
                weight = random.randint(1, max_weight)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph

# Measure execution time of Kruskal's algorithm
def measure_kruskal(graph, num_vertices):
    start_time = time.time()
    kruskal(graph, num_vertices)
    return time.time() - start_time

# Measure execution time of Prim's algorithm
def measure_prims(graph, start):
    start_time = time.time()
    prims(graph, start)
    return time.time() - start_time

# Main comparison function
def compare_algorithms(vertex_sizes, density=0.5):
    kruskal_times = []
    prims_times = []

    for num_vertices in vertex_sizes:
        graph = generate_graph(num_vertices, density)

        # Measure Kruskal's execution time
        kruskal_time = measure_kruskal(graph, num_vertices)
        kruskal_times.append(kruskal_time)

        # Measure Prim's execution time
        prims_time = measure_prims(graph, 0)  # Start from vertex 0
        prims_times.append(prims_time)

    return kruskal_times, prims_times

# Ask user for vertex sizes
vertex_sizes = input("Enter the list of vertex sizes separated by commas (e.g., 10,20,30): ")
vertex_sizes = [int(size.strip()) for size in vertex_sizes.split(",")]

# Compare algorithms
kruskal_times, prims_times = compare_algorithms(vertex_sizes)


# Plotting the results
sort_type1= "Kruskal's algorithm"
sort_type2 = "Prim's algorithm"

plot_graph2(vertex_sizes, kruskal_times, prims_times, sort_type1, sort_type2)
