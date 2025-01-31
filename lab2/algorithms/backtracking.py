def solve_nqueens_backtracking(n):
    """
    Solve the N-Queens problem using backtracking.
    :param n: The size of the chessboard (n x n).
    :return: A list of solutions, where each solution is a list representing the row positions of queens.
    """
    def is_safe(board, row, col):
        # Check this row on the left
        for i in range(col):
            if board[row][i] == "Q":
                return False

        # Check upper diagonal on the left
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        # Check lower diagonal on the left
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        return True

    def solve(col):
        # Base case: All queens are placed
        if col >= n:
            solutions.append(["".join(row) for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col):
                # Place the queen
                board[i][col] = "Q"

                # Recur to place rest of the queens
                solve(col + 1)

                # Backtrack: Remove the queen
                board[i][col] = "."

    # Initialize the chessboard
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(0)
    return solutions


def print_solutions(solutions):
    """
    Print all solutions in chessboard format.
    :param solutions: A list of solutions where each solution is a list of strings representing the board.
    """
    for idx, solution in enumerate(solutions, start=1):
        print(f"Solution {idx}:")
        for row in solution:
            print(row)
        print("\n")


n = int(input("Enter the value of N: "))
solutions = solve_nqueens_backtracking(n)

if not solutions:
    print("No solution exists.")
else:
    print_solutions(solutions)
    print(f"Found {len(solutions)} solutions:")
