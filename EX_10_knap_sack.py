"""
    Knap Sack Problem Implementation (Greedy Technique)

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

from tabulate import tabulate


class Knap_Sack:
    def __init__(self, M, N):
        self._max_capacity = M
        self._num_products = N
        self._data = {}

    def add_detail(self, product, profit, weight):
        self._data[product] = (profit, weight, round((profit / weight), 3))

    def solve_KS(self):
        self._data = dict(
            sorted(self._data.items(), key=lambda item: item[1][2], reverse=True)
        )

        total_profit = 0
        remaining = self._max_capacity
        details = []
        for data in self._data.items():
            if remaining == 0:
                break
            product = data[0]
            profit, weight, unit_profit = data[1]

            if weight > remaining:
                taken_unit = remaining / weight
            else:
                taken_unit = 1

            remaining -= weight * taken_unit

            taken_profit = profit * taken_unit

            details.append(
                [product, profit, weight, taken_unit, remaining, taken_profit]
            )

            total_profit += taken_profit

        self.display(details)
        print(f"Maximum Profit : {total_profit}")
        return total_profit

    def display(self, table):
        header = [
            "Product",
            "Profit",
            "Weight",
            "Taken unit",
            "Remaining",
            "Taken profit",
        ]
        print(tabulate(table, headers=header, tablefmt="grid"))

    def __str__(self):
        return str(self._data)

if __name__ == '__main__':
    K = Knap_Sack(15, 7)
    K.add_detail(1, 10, 2)
    K.add_detail(2, 5, 3)
    K.add_detail(3, 15, 5)
    K.add_detail(4, 7, 7)
    K.add_detail(5, 6, 1)
    K.add_detail(6, 18, 4)
    K.add_detail(7, 3, 1)
    K.solve_KS()
