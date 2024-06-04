"""
    Computing Binomial Coefficient (Dynamic Programming)

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2401 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

def Binomial_Coefficient(n, r, memo):
    if (n < r) or (n < 0 or r < 0):
        return 0
    
    if r == n or  r == 0:
        return 1
    
    if r == 1 or r == n - 1:
        return n
    
    if (n, r) in memo:
        return memo[(n, r)]

    result = Binomial_Coefficient(n - 1, r - 1, memo) + Binomial_Coefficient(n - 1, r, memo)
    memo[(n, r)] = result
    return result


if __name__ == "__main__":
    n, r = 50, 15
    memo = {}
    print(f"\n {n} C {r}  :=  ", Binomial_Coefficient(n, r, memo))
    print(f"Computed {len(memo)} values") 