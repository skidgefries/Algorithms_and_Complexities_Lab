import random
import time

def knapsack_01(values, weights, capacity, n):
    # Create a DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find the selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    return dp[n][capacity], selected_items

def generate_random_items(n):
    values = [random.randint(100, 1000) for _ in range(n)]
    weights = [random.randint(1, 10) for _ in range(n)]
    return values, weights

# User input
n = int(input("Enter the number of items: "))
choice = input("Do you want to enter values and weights manually? (yes/no): ").strip().lower()

if choice == "yes":
    values = list(map(int, input(f"Enter the values of {n} items separated by space: ").split()))
    weights = list(map(int, input(f"Enter the weights of {n} items separated by space: ").split()))
else:
    values, weights = generate_random_items(n)
    print("Generated values:", values)
    print("Generated weights:", weights)

capacity = int(input("Enter the capacity of the knapsack: "))


t1=time.time();
max_value, selected_items = knapsack_01(values, weights, capacity, n)
t2= time.time();

t3= t2 - t1
print(f"Maximum value in Knapsack: {max_value}")
print("Selected items (0-based index):", selected_items)
print(f"The total time taken is: {t3}")
