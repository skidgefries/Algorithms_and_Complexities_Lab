import time
import sys

sys.path.append("util")
from rannumgen import generate_random_numbers
from plot_inputVstime import plot_graph1

sys.path.append("lab1")
from algorithms.selectionsort import selection_sort
from algorithms.insertionsort import insertion_sort
from algorithms.mergesort import merge_sort
from algorithms.quicksort import quick_sort
from algorithms.heapsort import heap_sort

def analyze_sort(sort_type):
    try:
        user_input = input("Enter the input sizes separated by commas (e.g., 10,100,1000): ")
        test_sizes = [int(size.strip()) for size in user_input.split(",")]

        print(f"Analyzing {sort_type} for varying input sizes:")
        print("Input Size\tExecution Time (seconds)")

        sizes = []
        times = []

        # Select the sorting algorithm based on user choice
        for size in test_sizes:
            numbers = generate_random_numbers(size)

            start_time = time.time()
            
            if sort_type == 'Selection Sort':
                selection_sort(numbers)
            elif sort_type == 'Insertion Sort':
                insertion_sort(numbers)
            elif sort_type == 'Merge Sort':
                merge_sort(numbers)
            elif sort_type == 'Quick Sort':
                quick_sort(numbers)
            elif sort_type == 'Heap Sort':
                heap_sort(numbers)
            else:
                print("Invalid sort type!")
                return
            
            end_time = time.time()
            execution_time = end_time - start_time
            sizes.append(size)
            times.append(execution_time)

            print(f"{size}\t\t{execution_time:.6f}")

        plot_graph1(sizes, times, sort_type)

    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
    except Exception as e:
        print("An error occurred during analysis:", e)

def main():
    print("Choose a sorting algorithm:")
    print("1. Selection Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")
    print("5. Heap Sort")
    
    try:
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            analyze_sort('Selection Sort')
        elif choice == 2:
            analyze_sort('Insertion Sort')
        elif choice == 3:
            analyze_sort('Merge Sort')
        elif choice == 4:
            analyze_sort('Quick Sort')
        elif choice == 5:
            analyze_sort('Heap Sort')
        else:
            print("Invalid choice! Please choose a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
