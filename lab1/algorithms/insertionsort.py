import sys
sys.path.append("util")
from rannumgen import generate_random_numbers


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    try:
        count = int(input("Enter the number of random numbers to generate: "))
        print()
        numbers = generate_random_numbers(count)
        print("Original array:", numbers)
        print()
        sorted_numbers = insertion_sort(numbers)
        print("Sorted array:", sorted_numbers)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
