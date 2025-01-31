import time
import matplotlib.pyplot as plt
import sys

sys.path.append("util")
from rannumgen import generate_random_numbers
from plot_algoVstime import plot_bargraph

sys.path.append("lab1")
from algorithms.selectionsort import selection_sort
from algorithms.insertionsort import insertion_sort
from algorithms.mergesort import merge_sort
from algorithms.quicksort import quick_sort
from algorithms.heapsort import heap_sort


# Measure the time taken by a sorting algorithm
def measure_time(sort_function, numbers):
    start_time = time.time()
    sort_function(numbers)
    return time.time() - start_time

# Apply all sorts and plot execution times for the same input size
def apply_all_sorts(input_size):
    sizes = []  # List to store input sizes
    times = []  # List to store execution times
    sort_types = ['Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort']

    # Generate random numbers once for the given input size
    numbers = generate_random_numbers(input_size)

    # Measure execution times for each sorting algorithm
    for sort_type in sort_types:
        if sort_type == 'Selection Sort':
            execution_time = measure_time(selection_sort, numbers.copy())
        elif sort_type == 'Insertion Sort':
            execution_time = measure_time(insertion_sort, numbers.copy())
        elif sort_type == 'Merge Sort':
            execution_time = measure_time(merge_sort, numbers.copy())
        elif sort_type == 'Quick Sort':
            execution_time = measure_time(quick_sort, numbers.copy())
        elif sort_type == 'Heap Sort':
            execution_time = measure_time(heap_sort, numbers.copy())
        
        sizes.append(sort_type)  # Store the sorting algorithm name
        times.append(execution_time)  # Store the execution time

    # Call plot_bargraph to display the bar chart for all sorting algorithms
    plot_bargraph(sizes, times, 'Sorting Algorithms',input_size)

def main():
    try:
        # Ask the user for the number of inputs (input size)
        input_size = int(input("Enter the number of random numbers to generate and sort: "))
        
        # Apply all sorting algorithms and plot the execution times
        apply_all_sorts(input_size)
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
