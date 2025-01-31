import heapq  # For priority queue (min heap)

def prims(graph, start):
    n = len(graph)
    
    # To track which vertices are included in the MST
    in_mst = [False] * n
    
    # Priority queue to select the edge with the minimum weight
    min_heap = []
    
    # Add the edges from the starting vertex to the heap
    def add_edges(v):
        in_mst[v] = True
        for neighbor, weight in enumerate(graph[v]):
            if not in_mst[neighbor] and weight != 0:  # Only consider edges not in MST
                heapq.heappush(min_heap, (weight, v, neighbor))
    
    # Start with the given vertex
    add_edges(start)
    
    mst_edges = []  # List to store the edges in MST
    total_weight = 0  # To track the total weight of the MST
    
    while min_heap:
        # Get the minimum weight edge from the heap
        weight, u, v = heapq.heappop(min_heap)
        
        # If vertex v is already in MST, skip
        if in_mst[v]:
            continue
        
        # Add edge to MST and include vertex v
        mst_edges.append((u, v, weight))
        total_weight += weight
        
        # Add the edges of the newly included vertex to the heap
        add_edges(v)
    
    return mst_edges, total_weight

# Example Graph Representation (Adjacency Matrix)
graph = [
    [0, 3, 1, 6, 0, 0],
    [3, 0, 5, 0, 3, 0],
    [1, 5, 0, 5, 6, 0],
    [6, 0, 5, 0, 0, 2],
    [0, 3, 6, 0, 0, 6],
    [0, 0, 4, 2, 6, 0]
]

# Running Prim's algorithm
start_vertex = 0
mst_edges, total_weight = prims(graph, start_vertex)

print("Edges in the Minimum Spanning Tree (MST):")
for u, v, weight in mst_edges:
    print(f"Edge ({u} - {v}) with weight {weight}")

print(f"Total weight of the MST: {total_weight}")
