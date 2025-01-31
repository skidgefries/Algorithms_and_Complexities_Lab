class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    # Find with path compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # Union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

def kruskal(graph, num_vertices):
    # Convert adjacency matrix to list of edges
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):  # Only consider upper triangle (i < j)
            if graph[i][j] != 0:  # If there's an edge
                edges.append((i, j, graph[i][j]))  # Add edge (u, v, weight)
    
    # Sort edges based on their weight
    edges = sorted(edges, key=lambda edge: edge[2])
    
    # Create disjoint set
    ds = DisjointSet(num_vertices)
    
    mst_edges = []  # List to store edges in MST
    total_weight = 0  # Total weight of the MST
    
    # Process each edge in sorted order
    for u, v, weight in edges:
        # If adding this edge doesn't form a cycle, include it in the MST
        if ds.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
    
    return mst_edges, total_weight

# Example graph represented as an adjacency matrix
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

# Running Kruskal's algorithm
num_vertices = 9  # The graph has 9 vertices
mst_edges, total_weight = kruskal(graph, num_vertices)

print("Edges in the Minimum Spanning Tree (MST):")
for u, v, weight in mst_edges:
    print(f"Edge ({u} - {v}) with weight {weight}")

print(f"Total weight of the MST: {total_weight}")
