import random
import time
import matplotlib.pyplot as plt
import sys

# Add paths to the algorithm modules
sys.path.append("lab2")
from algorithms.backtracking import solve_nqueens_backtracking

sys.path.append("lab4")
from algorithms.lasvegas_nqueens import las_vegas_n_queens

sys.path.append("util")
from plot_inputVstime import plot_graph2

# Measure execution times for both algorithms
def measure_execution_times(n_values):
    backtracking_times = []
    las_vegas_times = []

    for n in n_values:
        # Backtracking
        start = time.time()
        solve_nqueens_backtracking(n)
        backtracking_times.append(time.time() - start)

        # Las Vegas
        start = time.time()
        las_vegas_n_queens(n)
        las_vegas_times.append(time.time() - start)

    return backtracking_times, las_vegas_times


# Plotting the comparison
sort_type1= "Backtracking"
sort_type2= "Las Vegas"
# plot_graph2(n_values, backtracking_times, las_vegas_times , sort_type1, sort_type2)
# def plot_comparison(n_values, backtracking_times, las_vegas_times):
#     plt.figure(figsize=(10, 6))
#     plt.plot(n_values, backtracking_times, label="Backtracking", marker='o')
#     plt.plot(n_values, las_vegas_times, label="Las Vegas", marker='x')
#     plt.title("Comparison of Backtracking and Las Vegas Algorithms for N-Queens")
#     plt.xlabel("N (Size of the Chessboard)")
#     plt.ylabel("Execution Time (seconds)")
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# Main function
def main():
    n_values = [8, 10, 12, 13]  # Sizes of the chessboard
    
    print("Measuring execution times...\n")
    backtracking_times, las_vegas_times = measure_execution_times(n_values)

    print("Execution Times (in seconds):")
    print(f"Backtracking: {backtracking_times}")
    print(f"Las Vegas: {las_vegas_times}")

    # plot_comparison(n_values, backtracking_times, las_vegas_times)
    plot_graph2(n_values, backtracking_times, las_vegas_times , sort_type1, sort_type2)

if __name__ == "__main__":
    main()
