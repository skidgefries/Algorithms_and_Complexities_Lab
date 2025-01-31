import numpy as np
import time
import random
import matplotlib.pyplot as plt
import multiprocessing

import sys
sys.path.append("util")
from rannumgen import generate_random_numbers
from plot_inputVstime import plot_graph2

sys.path.append("lab1")
from algorithms.quicksort import quick_sort

sys.path.append("lab4")
from algorithms.parallel_quick_sort import parallel_quicksort

def measure_sorting_time(sort_func, arr, **kwargs):
    """Measures execution time of a sorting function."""
    start_time = time.time()
    sort_func(arr.copy(), **kwargs)
    return time.time() - start_time

def plot_complexity_comparison():
    """Compares sequential and parallel quicksort performance."""
    sizes = np.linspace(800000, 10000000, 5, dtype=int)
    parallel_times = []
    sequential_times = []
    num_processes = multiprocessing.cpu_count()

    print(f"Running comparison using {num_processes} CPU cores...")

    for size in sizes:
        print(f"Testing size {size}")
        arr = generate_random_numbers(size)

        parallel_time = measure_sorting_time(
            parallel_quicksort, arr, num_processes=num_processes
        )
        sequential_time = measure_sorting_time(
            quick_sort, arr
        )

        print(f"Sequential: {sequential_time:.4f}s, Parallel: {parallel_time:.4f}s")
        print(f"Speedup: {sequential_time/parallel_time:.2f}x")

        parallel_times.append(parallel_time)
        sequential_times.append(sequential_time)
    
    sort_type1= 'Sequential Quicksort' 
    sort_type2= "Parallel Quicksort"

    plot_graph2(sizes, parallel_times, sequential_times , sort_type1, sort_type2)

    avg_speedup = np.mean([s / p for s, p in zip(sequential_times, parallel_times)])
    plt.text(0.02, 0.98, f'Average Speedup: {avg_speedup:.2f}x',
             transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', alpha=0.8))

    plt.show()

if __name__ == "__main__":
    plot_complexity_comparison()
