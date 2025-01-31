import sys
sys.path.append("util")
from rannumgen import generate_random_numbers


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        # Recursively apply quick_sort to the left and right parts and concatenate them
        return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    try:
        count = int(input("Enter the number of random numbers to generate: "))
        print()
        numbers = generate_random_numbers(count)
        print("Original array:", numbers)
        print()
        sorted_numbers = quick_sort(numbers)
        print("Sorted array:", sorted_numbers)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
