import random

def generate_activities(num_activities):
    start_times = []
    finish_times = []

    for _ in range(num_activities):
        start = random.randint(0, 20)  # Random start time between 0 and 20
        finish = random.randint(start + 1, start + 10)  # Finish time is always later than start time
        start_times.append(start)
        finish_times.append(finish)

    return start_times, finish_times

def activity_selection(start, finish):
    n = len(start)

    # Sort the activities based on finish times
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    # Unpack the sorted activities
    sorted_start, sorted_finish = zip(*activities)

    # The first activity is always selected
    selected_activities = [0]
    last_selected = 0  # The last selected activity index

    # Iterate through the remaining activities
    for i in range(1, n):
        if sorted_start[i] >= sorted_finish[last_selected]:
            selected_activities.append(i)
            last_selected = i

    return selected_activities, sorted_start, sorted_finish

# Main program
if __name__ == "__main__":
    try:
        num_activities = int(input("Enter the number of activities: "))
        start_times, finish_times = generate_activities(num_activities)

        print("Original Start Times:", start_times)
        print("Original Finish Times:", finish_times)

        selected, sorted_start, sorted_finish = activity_selection(start_times, finish_times)

        print("\nSorted Start Times:", sorted_start)
        print("Sorted Finish Times:", sorted_finish)

        print("\nSelected Activities (by index in sorted order):")
        for index in selected:
            print(f"Activity {index + 1}: Start = {sorted_start[index]}, Finish = {sorted_finish[index]}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
