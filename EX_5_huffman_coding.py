"""
    Huffmann Coding (Greedy Technique)

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 26 - 05- 2024
"""

import heapq
from collections import defaultdict


class Node:
    def __init__(self, value, char=None, left=None, right=None):
        """Initialize a Node object."""
        self._value = value
        self._left = left
        self._right = right
        self._char = char

    def __lt__(self, other):
        """Define less-than for Node objects to be used in heapq."""
        return self._value < other._value


def get_freq_dict(message):
    """Create a dictionary of character frequencies in the message."""
    freq_dict = defaultdict(int)
    print(freq_dict)
    for char in message:
        freq_dict[char] += 1
    return freq_dict


def construct_tree(message):
    """Construct the Huffman tree for the given message."""
    # Create a dictionary of character frequencies
    freq_dict = get_freq_dict(message)

    # Create a priority queue (min-heap) of nodes for each character
    heap = [Node(value, char) for char, value in freq_dict.items()]
    heapq.heapify(heap)

    # Construct the Huffman tree
    while len(heap) > 1:
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        new_node = Node(min1._value + min2._value)
        new_node._left = min1
        new_node._right = min2
        heapq.heappush(heap, new_node)

    return heapq.heappop(heap)


def get_huffman_codes(node, code="", codes={}):
    """Generate Huffman codes for each character."""
    if node is None:
        return {}

    if node._char is not None:
        codes[node._char] = code
        return codes

    get_huffman_codes(node._left, code + "0", codes)
    get_huffman_codes(node._right, code + "1", codes)

    return codes


if __name__ == "__main__":
    message = input("\nEnter the message: ")
    tree = construct_tree(message)
    codes = get_huffman_codes(tree)
    codes = {
        key: value
        for key, value in sorted(codes.items(), key=lambda item: len(item[1]))
    }  # sort based on code length

    print("\n" + "=" * 20)
    for character, code in codes.items():
        print(f"{character} ---> {code}")
    print("=" * 20 + "\n")

    huffman_code = ""
    for char in message:
        huffman_code += codes[char]

    actual_size = len(message) * 8
    code_size = len(huffman_code)

    print("Huffman Code: ", huffman_code)
    print("Actual Size: ", actual_size)
    print("Total Size: ", code_size)
    print("Percentage of Optimization: ", (1 - (code_size / actual_size)) * 100, "%")
