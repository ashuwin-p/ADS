"""
    Knap Sack Problem Implementation (Greedy Technique)

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

from tabulate import tabulate


class Product:
    def __init__(self, item_no, profit, weight):
        self.item_no = item_no
        self.profit = profit
        self.weight = weight
        self.ratio = round(profit / weight, 3)

    def __lt__(self, other):
        return self.ratio < other.ratio

    def __str__(self):
        return str(self.item_no)


class Knap_Sack:
    def __init__(self, M, N):
        self._max_capacity = M
        self._num_products = N
        self._data = []

    def add_product(self, item_no, profit, weight):
        product = Product(item_no, profit, weight)
        self._data.append(product)

    def solve_KS(self):
        self._data = sorted(self._data, reverse=True)

        total_profit = 0
        remaining = self._max_capacity
        details = []
        for product in self._data:
            if remaining == 0:
                break

            if product.weight > remaining:
                taken_unit = remaining / product.weight
            else:
                taken_unit = 1

            remaining -= product.weight * taken_unit

            taken_profit = product.profit * taken_unit

            details.append(
                [
                    product.item_no,
                    product.profit,
                    product.weight,
                    taken_unit,
                    remaining,
                    taken_profit,
                ]
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
        return str([str(product) for product in self._data])


if __name__ == "__main__":
    K = Knap_Sack(15, 7)
    K.add_product(1, 10, 2)
    K.add_product(2, 5, 3)
    K.add_product(3, 15, 5)
    K.add_product(4, 7, 7)
    K.add_product(5, 6, 1)
    K.add_product(6, 18, 4)
    K.add_product(7, 3, 1)
    K.solve_KS()
