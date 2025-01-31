import itertools
import random
import time

# Function to calculate the total distance of a given route
def calculate_distance(route, graph):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += graph[route[i]][route[i + 1]]
    # Return to the starting city
    total_distance += graph[route[-1]][route[0]]
    return total_distance

# Traveling Salesman Problem (TSP) using brute force
def tsp_bruteforce(graph):
    n = len(graph)
    cities = list(range(n))
    
    # Generate all possible permutations of cities
    min_distance = float('inf')
    best_route = None
    
    for perm in itertools.permutations(cities):
        distance = calculate_distance(perm, graph)
        if distance < min_distance:
            min_distance = distance
            best_route = perm
    
    return best_route, min_distance

# Function to generate a random adjacency matrix
def generate_graph(num_cities, max_distance=100):
    graph = [[0 if i == j else random.randint(1, max_distance) for j in range(num_cities)] for i in range(num_cities)]
    return graph

# Main Function
def main():
    # Ask user for the number of cities
    num_cities = int(input("Enter the number of cities: "))
    if num_cities < 2:
        print("Number of cities must be at least 2.")
        return

    # Generate a random graph
    graph = generate_graph(num_cities)
    
    print("\nGenerated Distance Matrix:")
    for row in graph:
        print(row)

    # Solve TSP
    t1= time.time()
    best_route, min_distance = tsp_bruteforce(graph)
    t2=time.time()
    t3=t2-t1

    print("\nBest route:", best_route)
    print("Minimum distance:", min_distance)
    print("Total time taken to solve it:", t3)

# Run the main function
if __name__ == "__main__":
    main()
