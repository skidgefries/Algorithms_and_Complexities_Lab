# Tabulation (Bottom-up approach)

import time
def get_fibonacci_tab(n):
    if n <= 1:
        return [0] if n == 0 else [0, 1]
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp

# Example of usage
n= int(input("Input the number: ")) 
t1= time.time()
fibonacci_series = get_fibonacci_tab(n)
t2=time.time()

print(f"The Tabulation Fibonacci series up to {n} is: {fibonacci_series}")

print(f"The total time taken is : {t2-t1} seconds")
