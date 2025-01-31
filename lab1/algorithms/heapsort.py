import sys
sys.path.append("util")
from rannumgen import generate_random_numbers


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than root or left child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n-1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]
        # Call heapify on the reduced heap
        heapify(arr, i, 0)

    return arr

if __name__ == "__main__":
    try:
        count = int(input("Enter the number of random numbers to generate: "))
        print()
        numbers = generate_random_numbers(count)
        print("Original array:", numbers)
        print()
        sorted_numbers = heap_sort(numbers)
        print("Sorted array:", sorted_numbers)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
