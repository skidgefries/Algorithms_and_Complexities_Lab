from itertools import permutations

def is_valid(queens):
    """
    Check if the given arrangement of queens is valid.
    :param queens: A tuple where each index represents a column, and the value represents the row of the queen.
    :return: True if the arrangement is valid, False otherwise.
    """
    n = len(queens)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if two queens are on the same diagonal
            if abs(queens[i] - queens[j]) == abs(i - j):
                return False
    return True

def solve_nqueens_bruteforce(n):
    """
    Solve the N-Queens problem using brute force.
    :param n: The size of the chessboard (n x n).
    :return: A list of solutions, where each solution is a tuple representing the row positions of queens.
    """
    all_permutations = permutations(range(n))  # Generate all possible permutations of queen positions
    valid_solutions = []

    for queens in all_permutations:
        if is_valid(queens):
            valid_solutions.append(queens)

    return valid_solutions

def print_solution(solution):
    """
    Print a single solution in chessboard format.
    :param solution: A tuple representing the row positions of queens.
    """
    n = len(solution)
    for row in solution:
        print(" ".join("Q" if i == row else "." for i in range(n)))
    print("\n")

n = int(input("Enter the value of N: "))
solutions = solve_nqueens_bruteforce(n)

if not solutions:
    print("No solution exists.")
else:
    for solution in solutions:
        print_solution(solution)
    print(f"Found {len(solutions)} solutions:")
