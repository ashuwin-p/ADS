"""
    N-Queens (Backtracking Approach)

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

from copy import deepcopy
from tabulate import tabulate

def isSafe(row, col, grid):
    n = len(grid) - 1

    # checking row horizontally
    c = col
    while c > 0:
        c -= 1
        if grid[row][c] == "Q":
            return False

    # Checking Top Diagonal
    r, c = row, col
    while (r > 0) and (c > 0):
        r -= 1
        c -= 1
        if grid[r][c] == "Q":
            return False

    # checking bottom diagonal
    r, c = row, col
    while (r < n) and (c > 0):
        r += 1
        c -= 1
        if grid[r][c] == "Q":
            return False
    return True

def Nqueens(n):
    def solve(n, col, grid, solutions):
        if col == n:
            answer = deepcopy(grid)
            solutions.append(answer)
            return

        for row in range(n):
            if isSafe(row, col, grid):
                grid[row][col] = "Q"
                solve(n, col + 1, grid, solutions)
                grid[row][col] = None  # Backtrack

        return solutions

    grid = [[None for _ in range(n)] for _ in range(n)]
    return solve(n, 0, grid, [])

# Example usage
ans = Nqueens(4)
i = 1
for soln in ans:
    print(f"Solution {i}:\n")
    print(tabulate(soln, tablefmt="grid"))
    i += 1
