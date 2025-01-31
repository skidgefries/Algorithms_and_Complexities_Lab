import multiprocessing
import sys
sys.path.append("lab1")
from algorithms.quicksort import quick_sort

def parallel_partition(data):
    """Helper function to sort chunks of data in parallel."""
    return quick_sort(data)

def merge_sorted_arrays(arrays):
    """Merge multiple sorted arrays into a single sorted array."""
    result = []
    indices = [0] * len(arrays)

    while True:
        min_val = float('inf')
        min_idx = -1

        # Find the smallest value among current positions
        for i in range(len(arrays)):
            if indices[i] < len(arrays[i]) and arrays[i][indices[i]] < min_val:
                min_val = arrays[i][indices[i]]
                min_idx = i

        if min_idx == -1:  # All arrays are exhausted
            break

        result.append(min_val)
        indices[min_idx] += 1

    return result

def parallel_quicksort(arr, num_processes=None):
    """Parallel quicksort using multiprocessing."""
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()  # Use available CPU cores

    if len(arr) < 1000:
        return quick_sort(arr)

    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    with multiprocessing.Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(parallel_partition, chunks)

    return merge_sorted_arrays(sorted_chunks)
