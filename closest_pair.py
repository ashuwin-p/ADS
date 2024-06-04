"""
    Computing Binomial Coefficient (Dynamic Programming)

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2401 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

global memo_table
memo_table = {}


def Binomial_Coefficient(n, r):
    if (n < r) or (n < 0 or r < 0):
        return 0

    elif n == r:
        return 1

    elif r == 1:
        return n

    elif r == n - 1:
        return n

    elif (n, r) in memo_table:
        return memo_table[(n, r)]

    result = Binomial_Coefficient(n - 1, r - 1) + Binomial_Coefficient(n - 1, r)
    memo_table[(n, r)] = result
    return result


if __name__ == "__main__":
    n, r = 6, 4
    print(f"\n {n} C {r}  :=  ", Binomial_Coefficient(n, r))
    print(f"Computed {len(memo_table)} values")
