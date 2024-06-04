"""
    Merge Sort Implementation

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2401 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

from copy import deepcopy


def merge_sort(lst):
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
    first_half = lst[:mid]
    second_half = lst[mid:]
    print(f"Dividing {lst} => {first_half}  ,  {second_half}")
    return merge(merge_sort(first_half), merge_sort(second_half))


def merge(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.

    Args:
        lst1 (list): The first sorted list.
        lst2 (list): The second sorted list.

    Returns:
        list: The merged and sorted list.
    """
    print(f"\nSorting: {lst1}  ,  {lst2}")
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

    print("Sorted: ", result, "\n")

    return result


if __name__ == "__main__":
    lst = [7, 3, 9, 1, 4, 6, 8, 5, 2, 10]
    print(f"\nInput List : {lst} \n")
    result = merge_sort(lst)
