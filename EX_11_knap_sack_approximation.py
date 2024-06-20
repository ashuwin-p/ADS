"""
    Approximation Algorithm - Knap Sack

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 20 - 06- 2024
"""
class Product:
    def __init__(self, item_no, profit, weight):
        self.item_no = item_no
        self.profit = profit
        self.weight = weight
        self.ratio = self.profit / self.weight

    def __lt__(self, other):
        return self.ratio < other.ratio
    
    def __str__(self):
        return str(self.item_no)

class KnapSack:
    def __init__(self, max_capacity, products):
        self.max_capacity = max_capacity
        self.products = products
        self.num_items = len(self.products)

    def solve(self):
        products = sorted(self.products, reverse=True)
        max_profit = 0
        current_weight = 0
        bag = []
        for product in products:
            if current_weight + product.weight < self.max_capacity:
                bag.append(product)
                current_weight += product.weight
                max_profit += product.profit
            else:
                break
        return bag, max_profit
    
if __name__ == '__main__':
    p1 = Product(1, 10, 5)
    p2 = Product(2, 8, 3)
    p3 = Product(3, 20, 2)
    p4 = Product(4, 5, 6)
    p5 = Product(5, 5, 15)
    p6 = Product(6, 20, 1)
    products = [p1, p2, p3, p4, p5, p6]

    KS = KnapSack(10, products)
    items, profit = KS.solve()
    for item in items:
        print(item)
    print("Maximum Profit : ", profit)
    