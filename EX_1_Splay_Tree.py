"""
    Splay Tree Implementation

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 20 - 06- 2024
"""

class TreeException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class SplayTree:
    def __init__(self, rootVal):
        """Initialize the SplayTree with a root value."""
        rootNode = Node(rootVal)
        self.root = rootNode

    def insert(self, value, node=None):
        """Insert a value into the SplayTree."""
        if node is None:
            node = self.root

        if value < node.value:
            if node.left is None:
                newNode = Node(value)
                node.left = newNode
                newNode.parent = node
                self.splay(newNode)  # Splay the newly inserted node
                print(f"Inserted Node {value}")
            else:
                self.insert(value, node.left)
        else:
            if node.right is None:
                newNode = Node(value)
                node.right = newNode
                newNode.parent = node
                self.splay(newNode)  # Splay the newly inserted node
                print(f"Inserted Node {value}")
            else:
                self.insert(value, node.right)

    def LeftRotate(self, node):
        """Perform a left rotation around the given node."""
        temp = node.right
        node.right = temp.left

        if temp.left is not None:
            temp.left.parent = node

        temp.parent = node.parent

        if node.parent is None:
            self.root = temp  # Update root if necessary
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp

        temp.left = node
        node.parent = temp

    def RightRotate(self, node):
        """Perform a right rotation around the given node."""
        temp = node.left
        node.left = temp.right

        if temp.right is not None:
            temp.right.parent = node

        temp.parent = node.parent

        if node.parent is None:
            self.root = temp  # Update root if necessary
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp

        temp.right = node
        node.parent = temp

    def splay(self, node):
        """Splay the given node to the root."""
        while node.parent is not None:
            parent = node.parent
            gp = parent.parent

            if gp is None:
                if node == parent.left:
                    self.RightRotate(parent)
                else:
                    self.LeftRotate(parent)

            elif node == parent.left and parent == gp.left:
                self.RightRotate(gp)
                self.RightRotate(parent)

            elif node == parent.right and parent == gp.right:
                self.LeftRotate(gp)
                self.LeftRotate(parent)

            elif node == parent.left and parent == gp.right:
                self.RightRotate(parent)
                self.LeftRotate(gp)

            else:
                self.LeftRotate(parent)
                self.RightRotate(gp)

        self.root = node  # Update root to splayed node

    def search(self, value, node=None):
        """Search for a value in the SplayTree and splay the found node to the root."""
        if node is None:
            node = self.root

        if node.value == value:
            print(f"Found Node {value}")
            self.splay(node)  # Splay the found node
            return self.root
        
        elif value < node.value:
            if node.left is not None:
                return self.search(value, node.left)
            else:
                raise TreeException(
                    f"(Search Result) : Node with value {value} not Found."
                )
            
        else:
            if node.right is not None:
                return self.search(value, node.right)
            else:
                raise TreeException(
                    f"(Search Result) : Node with value {value} not Found"
                )

    def delete(self, value):
        """Delete a node with the given value from the SplayTree."""
        try:
            self.search(value)
            node = self.root  # Node to be deleted is now the root

            if node.left is None and node.right is None:
                self.root = None  # No children case
            elif node.left is not None and node.right is not None:
                max_lst = node.left
                while max_lst.right is not None:
                    max_lst = max_lst.right

                node.value = max_lst.value  # Replace value with max of left subtree

                # Remove max_lst
                if max_lst.left is not None:
                    if max_lst.parent.left == max_lst:
                        max_lst.parent.left = max_lst.left
                    else:
                        max_lst.parent.right = max_lst.left
                    max_lst.left.parent = max_lst.parent
                else:
                    if max_lst.parent.left == max_lst:
                        max_lst.parent.left = None
                    else:
                        max_lst.parent.right = None

                print(f"Deleted Node {value}")

            elif node.right is not None:
                self.root = node.right  # Single right child case
                node.right.parent = None
                
            else:
                self.root = node.left  # Single left child case
                node.left.parent = None

            print(f"Deleted Node {value}")
        except TreeException:
            raise TreeException(
                f"(Deletion result) : Node with value {value} not Found, Deletion Failed"
            )

    def preorder(self, node):
        """Perform preorder traversal starting from the given node."""
        if node is None:
            return

        print(node)
        self.preorder(node.left)
        self.preorder(node.right)

    def getRoot(self):
        """Return the root of the SplayTree."""
        return self.root


if __name__ == "__main__":
    try:
        tree = SplayTree(10)
        tree.insert(20)
        tree.insert(25)
        tree.insert(5)
        tree.insert(40)
        tree.search(5)
        tree.delete(10)
        root = tree.getRoot()
        print("\n\n Pre Order Traversal")
        tree.preorder(root)
    except TreeException as e:
        print(e)
