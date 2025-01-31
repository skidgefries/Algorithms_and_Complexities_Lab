import random

# Check if the position is safe for a queen
def is_safe_las_vegas(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

# Las Vegas algorithm for N-Queens
def las_vegas_n_queens(n):
    attempts = 0
    while True:
        attempts += 1
        board = [-1] * n  # Initialize board with no queens placed
        for row in range(n):
            valid_positions = [col for col in range(n) if is_safe_las_vegas(board, row, col, n)]
            if not valid_positions:  # If no valid position is found, retry
                break
            board[row] = random.choice(valid_positions)  # Randomly place a queen
        if -1 not in board:  # Solution is found if all rows have queens
            return board, attempts

# Print the chessboard solution
def print_board(board):
    n = len(board)
    for row in board:
        line = ['.'] * n
        line[row] = 'Q'
        print(" ".join(line))
    print("\n")

# # Main function
if __name__ == "__main__":
    n = int(input("Enter the value of N: "))
    if n < 1:
        print("N must be at least 1.")
    else:
        solution, attempts = las_vegas_n_queens(n)
        print_board(solution)
        print(f"Solution found in {attempts} attempts:\n")
