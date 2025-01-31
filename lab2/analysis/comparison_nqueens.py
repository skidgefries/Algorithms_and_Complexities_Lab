import time
import matplotlib.pyplot as plt
import sys

sys.path.append("lab2")
from algorithms.backtracking import solve_nqueens_backtracking
from algorithms.bruteforcenqueens import solve_nqueens_bruteforce

sys.path.append("util")
from plot_inputVstime import plot_graph2

# Measure execution time of a solver 
def measure_time(solver, n):
    start_time = time.time()
    solver(n)
    end_time = time.time()
    return end_time - start_time

# Compare algorithms and plot results
def compare_algorithms():
    try:
        # Ask user for input values of N
        user_input = input("Enter values of N separated by commas (e.g., 4,5,6): ")
        n_values = [int(n.strip()) for n in user_input.split(",")]
        
        brute_times = []
        backtrack_times = []

        for n in n_values:
            print(f"\nTesting for N={n}...")

            # Measure time for brute-force
            try:
                brute_time = measure_time(solve_nqueens_bruteforce, n)
                brute_times.append(brute_time)
                print(f"Brute-Force: {brute_time:.4f} sec")
            except Exception as e:
                brute_times.append(float("nan"))
                print(f"Error in Brute-Force for N={n}: {e}")

            # Measure time for backtracking
            try:
                backtrack_time = measure_time(solve_nqueens_backtracking, n)
                backtrack_times.append(backtrack_time)
                print(f"Backtracking: {backtrack_time:.4f} sec")
            except Exception as e:
                backtrack_times.append(float("nan"))
                print(f"Error in Backtracking for N={n}: {e}")

        # Plotting results

        sort_type1="Brute-Force"
        sort_type2="Backtracking"
        plot_graph2(n_values, brute_times, backtrack_times , sort_type1, sort_type2)


    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    compare_algorithms()
