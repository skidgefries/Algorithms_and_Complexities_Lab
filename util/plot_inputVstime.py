import matplotlib.pyplot as plt

def plot_graph1(sizes, times, sort_type):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title(f"{sort_type}: Input Size vs Execution Time")
    plt.grid(True)
    plt.show()

def plot_graph2(vertex_sizes, times1, times2 , sort_type1, sort_type2):
    plt.figure(figsize=(10, 6))
    plt.plot(vertex_sizes, times1, label=f"{sort_type1}", marker='o')
    plt.plot(vertex_sizes, times2, label=f"{sort_type2}", marker='s')
    plt.title(f"Comparison of {sort_type1} and {sort_type2}")
    plt.xlabel("Number of Inputs")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()
