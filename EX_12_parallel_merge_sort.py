"""
    Merge Sort (parallel) Implementation
 
    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 20 - 06 - 2024
"""

from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor as TPE

def merge_sort(lst, max_workers = 2):
    """
    Sorts a list using the merge sort algorithm.

    Args:
        lst (list): The list to be sorted.

    Returns:
        list: A new sorted list.
    """
    if len(lst) <= 1:
        return deepcopy(lst)

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    with TPE (max_workers=max_workers)as executor:
        left_sorted = executor.submit(merge_sort, left, max_workers).result()
        right_sorted = executor.submit(merge_sort, right, max_workers).result()
    return merge(left_sorted, right_sorted)


def merge(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.

    Args:
        lst1 (list): The first sorted list.
        lst2 (list): The second sorted list.

    Returns:
        list: The merged and sorted list.
    """
    n1, n2 = len(lst1), len(lst2)
    p1, p2 = 0, 0  # initial pointer position
    result = []

    while p1 < n1 and p2 < n2:
        if lst1[p1] < lst2[p2]:
            result.append(lst1[p1])
            p1 += 1
        else:
            result.append(lst2[p2])
            p2 += 1

    if p1 < n1:  # remaining elements
        result.extend(lst1[p1:])
    if p2 < n2:
        result.extend(lst2[p2:])

    return result


if __name__ == "__main__":
    lst = [7, 3, 9, 1, 4, 6, 8, 5, 2, 10]
    print(f"\nInput List : {lst} \n")
    result = merge_sort(lst)
    print("Sorted List : ",result)
