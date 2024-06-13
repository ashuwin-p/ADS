class SplayTree:
    class Node:
        def __init__(self, value, parent=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent

    def __init__(self, item):
        if item is not None:
            self.root = self.Node(item)

    def add_left(self, item, parent):
        left_node = self.Node(item, parent)
        parent.left = left_node

    def add_right(self, item, parent):
        right_node = self.Node(item, parent)
        parent.right = right_node

    def insert(self, value, root):
        new_node = self.Node(value)
        if value == root.value:
            return

        if value < root.value:
            if root.left is not None:
                self.insert(value, root.left)
            else:
                root.left = new_node
                new_node.parent = root
                self.splay(new_node)
        else:
            if root.right is not None:
                self.insert(value, root.right)
            else:
                root.right = new_node
                new_node.parent = root
                self.splay(new_node)

    def splay(self, node):
        while node.parent is not None:
            parent = node.parent
            grandparent = parent.parent

            if grandparent is None:
                if node == parent.left:
                    self.right_rotate(parent)
                else:
                    self.left_rotate(parent)
            elif node == parent.left and parent == grandparent.left:
                self.right_rotate(grandparent)
                self.right_rotate(parent)
            elif node == parent.right and parent == grandparent.right:
                self.left_rotate(grandparent)
                self.left_rotate(parent)
            elif node == parent.right and parent == grandparent.left:
                self.left_rotate(parent)
                self.right_rotate(grandparent)
            else:
                self.right_rotate(parent)
                self.left_rotate(grandparent)

        self.root = node

    def left_rotate(self, node):
        temp = node.right
        node.right = temp.left
        if temp.left is not None:
            temp.left.parent = node

        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp

        temp.left = node
        node.parent = temp

    def right_rotate(self, node):
        temp = node.left
        node.left = temp.right
        if temp.right is not None:
            temp.right.parent = node

        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp

        temp.right = node
        node.parent = temp

    def search(self, tree, value):
        if tree.value == value:
            self.splay(tree)
            return self.root

        elif value < tree.value:
            if tree.left is not None:
                return self.search(tree.left, value)
            else:
                self.splay(tree)
                return None
        else:
            if tree.right is not None:
                return self.search(tree.right, value)
            else:
                self.splay(tree)
                return None

    def delete(self, value):
        node = self.search(self.root, value)
        if node is None:
            return False
        else:
            if node.left:
                max_left = node.left
                while max_left.right:
                    max_left = max_left.right
                self.splay(max_left)

                max_left.right = node.right
                if node.right:
                    node.right.parent = max_left
            else:
                self.root = node.right
                if node.right:
                    node.right.parent = None
            return True

    def preorder(self, node):
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)


if __name__ == "__main__":
    tree = SplayTree(22)
    print("Inorder traversal")
    tree.insert(15, tree.root)
    tree.insert(11, tree.root)
    tree.insert(23, tree.root)
    # tree.insert(33, tree.root)
    # tree.insert(28, tree.root)
    # tree.insert(43, tree.root)
    # tree.preorder(tree.root)
    
    print("-----------------------")
    tree.delete(23)
    print("After deletion")
    tree.preorder(tree.root)

    print("Visualizing the Splay Tree:")
    tree.draw_tree(tree.root)
