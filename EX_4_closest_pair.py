"""
    Closest Pair of Points (Divide and Conquer approach)

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

import math
import random

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p1._x - p2._x)**2 + (p1._y - p2._y)**2)

    def __str__(self):
        return f"({self._x}, {self._y})"



def closest_pair(Px, Py):
    # base case
    if len(Px) < 4:
        return bruteforce_closest_pair(Px)

    # Divide the points sorted based on X axis into Two Halves
    mid = len(Px) // 2
    L = Px[:mid]
    R = Px[mid:]

    # Sort Left and Right Halves by both X and Y coordinates
    Lx = sorted(L, key=lambda p: p._x)
    Ly = sorted(L, key=lambda p: p._y)
    Rx = sorted(R, key=lambda p: p._x)
    Ry = sorted(R, key=lambda p: p._y)

    # Recursively find closest pair on Left and Right halves (points sorted based on x axis)
    left_min, p1, q1 = closest_pair(Lx, Ly)
    right_min, p2, q2 = closest_pair(Rx, Ry)
    d = min(left_min, right_min)

    # Finding closest pair between Left and Right half
    split_min, p3, q3 = closest_split_pair(Px, Py, d)

    # Find the minimum and return the closest pair of points
    minimum = min(left_min, right_min, split_min)

    if minimum == left_min:
        return left_min, p1, q1
    elif minimum == right_min:
        return right_min, p2, q2
    else:
        return split_min, p3, q3

def bruteforce_closest_pair(points):
    min_dist = float('inf')
    p, q = None, None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = Point.distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                p, q = points[i], points[j]
                
    return min_dist, p, q


def closest_split_pair(Px, Py, d):
    # Initialize minimum distance and pair
    min_strip_dist = float('inf')
    p, q = None, None
    
    # Get the point in the boundary x-coordinate
    xbar = Px[len(Px) // 2]._x

    # Get all the points between xbar - d and xbar + d sorted by y-coordinates
    Sy = []
    for point in Py:
        if xbar - d <= point._x <= xbar + d:
            Sy.append(point)

    # Iterate over points in Sy
    for i in range(len(Sy)):
        for j in range(i + 1, min(i + 8, len(Sy))):
            dist = Point.distance(Sy[i], Sy[j])
            if dist < min_strip_dist:
                min_strip_dist = dist
                p, q = Sy[i], Sy[j]

    # Return the minimum distance and the pair of points
    return min_strip_dist, p, q


if __name__ == '__main__':
    points = []
    for i in range(100):
        pt = Point(random.randint(-100, 100), random.randint(-100, 100))
        points.append(pt)

    Px = sorted(points, key=lambda p: p._x)
    Py = sorted(points, key=lambda p: p._y)

    dist, p, q = closest_pair(Px, Py)
    print("Pair of Points : ", p, q)
    print("Distance       : ", dist)