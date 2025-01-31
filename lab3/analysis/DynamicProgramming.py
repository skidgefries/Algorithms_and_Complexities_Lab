import time
import matplotlib.pyplot as plt
import sys

# Add directories for importing algorithms and utilities
sys.path.append("lab3")
from algorithms.fibonacciseries_recursion import fibonacci_recursive
from algorithms.fibonacciseries_tabulation import get_fibonacci_tab

sys.path.append("util")
from plot_inputVstime import plot_graph2

# Measure execution time for both methods
def measure_execution_time(n_values):
    recursive_times = []
    tab_times = []

    for n in n_values:
        # Measure time for recursion (only for smaller n due to inefficiency)
        if n <= 40:  # Recursion becomes infeasible for large n
            start = time.time()
            fibonacci_recursive(n)
            recursive_times.append(time.time() - start)
        else:
            recursive_times.append(None)  # Skipped for large n

        # Measure time for tabulation
        start = time.time()
        get_fibonacci_tab(n)
        tab_times.append(time.time() - start)

    return recursive_times, tab_times

# Main function
def main():
    # n_values = [10, 20, 25, 30]  # Values for testing
    user_input = input("Enter Fibonacci series lengths separated by commas (e.g., 10,20,30): ")
    try:
        n_values = [int(value.strip()) for value in user_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter integers separated by commas.")
        return
    recursive_times, tab_times = measure_execution_time(n_values)

    print("Execution Times:")
    print(f"Recursion: {recursive_times}")
    print(f"Tabulation: {tab_times}")

    sort_type1 = "Recursive"
    sort_type2 = "Tabulation"
    plot_graph2(n_values, recursive_times, tab_times, sort_type1, sort_type2)

if __name__ == "__main__":
    main()
