"""
    Computing Binomial Coefficient (Dynamic Programming)

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""


def Binomial_Coefficient(n, r, memo):
    # Base cases
    if (n < r) or (n < 0 or r < 0):  # Invalid input cases
        return 0

    if r == n or r == 0:  # Base case: nC0 or nCn
        return 1

    if r == 1 or r == n - 1:  # Base case: nC1 or nC(n-1)
        return n

    if (n, r) in memo:  # Check if result is already computed
        return memo[(n, r)]

    # Recursive calculation with memoization
    result = Binomial_Coefficient(n - 1, r - 1, memo) + Binomial_Coefficient(
        n - 1, r, memo
    )
    memo[(n, r)] = result  # Store computed result in memo

    return result


if __name__ == "__main__":
    n, r = 50, 15
    memo = {}  # Dictionary to store computed values for memoization
    print(f"\n {n} C {r}  :=  ", Binomial_Coefficient(n, r, memo))
    print(f"Computed {len(memo)} values")  # Output the number of computed values
