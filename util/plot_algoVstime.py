import matplotlib.pyplot as plt

def plot_bargraph(sizes, times, sort_type, n):
    # Plotting the bar graph
    plt.bar(sizes, times, color='coral')
    
    
    # Adding labels and title
    plt.xlabel('Algorithms')
    plt.ylabel('Execution Time (seconds)')
    plt.title(f"Execution Time of different algorithms for {n} inputs")

    # Show grid and plot
    # plt.grid(True)
    plt.show()
