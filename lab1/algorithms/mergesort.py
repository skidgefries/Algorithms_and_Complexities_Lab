import sys
sys.path.append("util")
from rannumgen import generate_random_numbers


def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively split and merge the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves back into the original array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

if __name__ == "__main__":
    try:
        count = int(input("Enter the number of random numbers to generate: "))
        print()
        numbers = generate_random_numbers(count)
        print("Original array:", numbers)
        print()
        sorted_numbers = merge_sort(numbers)
        print("Sorted array:", sorted_numbers)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
