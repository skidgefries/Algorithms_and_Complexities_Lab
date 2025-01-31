import time
import matplotlib.pyplot as plt
import sys
sys.path.append("lab2")
from algorithms.activityselection import activity_selection, generate_activities


sys.path.append("util")
from plot_inputVstime import plot_graph1
# Function to measure execution time of activity selection
def measure_time(num_activities):
    start_times, finish_times = generate_activities(num_activities)

    start_time = time.time()
    activity_selection(start_times, finish_times)
    end_time = time.time()

    return end_time - start_time

# Main function to analyze performance and plot results

def analyze_activity_selection():
    try:
        # Ask user for input sizes
        user_input = input("Enter the numbers of activities separated by commas (e.g., 10,20,50): ")
        input_sizes = [int(size.strip()) for size in user_input.split(",")]

        execution_times = []

        # Measure execution time for each input size
        for num_activities in input_sizes:
            print(f"Measuring for {num_activities} activities...")
            exec_time = measure_time(num_activities)
            execution_times.append(exec_time)

        # Plot the results
        sort_type = "Activity Selection"
        plot_graph1(input_sizes, execution_times, sort_type)

    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    analyze_activity_selection()
