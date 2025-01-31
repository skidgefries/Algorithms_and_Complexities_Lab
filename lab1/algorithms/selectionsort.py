import sys
sys.path.append("util")
from rannumgen import generate_random_numbers

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the first element of the unsorted part is the smallest
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the smallest element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    try:
        count = int(input("Enter the number of random numbers to generate: "))
        print()
        numbers = generate_random_numbers(count)
        print("Original array:", numbers)
        print()
        sorted_numbers = selection_sort(numbers)
        print("Sorted array:", sorted_numbers)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
