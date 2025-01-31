# Recursion (without optimization)
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example of usage
n= int(input("Input the number: "))  # You can change this value for different Fibonacci numbers
fibonacci_series = [fibonacci_recursive(i) for i in range(n+1)]
print(f"The Recursive Fibonacci series up to {n} is: {fibonacci_series}")