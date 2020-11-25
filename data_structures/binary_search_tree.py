"""
Python implementation of binary search tree.

BST's time complexity is O(log n)

Binary search tree cannot have duplicate element.

"""


class BinarySearchTreeNode:
    """
    BST Node.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        """
        Method to add child node.
        """
        if data == self.data:
            # binary search tree cannot have a duplicate element
            return

        # add 'data' in left subtree
        if data < self.data:
            # if the data exists on left child
            if self.left:
                self.left.add_child(data)
            # if the left child is empty
            else:
                self.left = BinarySearchTreeNode(data)
        # add 'data' in right subtree
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        """
        In order traversal - visit left subtree -> Node -> right subtree
        :return: list of elements in a binary tree in specific order
        """
        elements = []

        # visit left tree first
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, value):
        """
        Search method for some value
        Search operation is easy now efficient, O(log n) search complexity.
        """
        if self.data == value:
            return True

        if value < self.data:
            # value might be in the left subtree
            if self.left:
                self.left.search(value)
            else:
                return False  # the value doesn't exist

        if value > self.data:
            # value might be in the right subtree
            if self.right:
                return self.right.search(value)
            else:
                return False


def build_tree(elements):
        root = BinarySearchTreeNode(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i])

        return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    # [1, 4, 9, 17, 18, 20, 23, 34]
    # set() -> removes duplicates BST can be useful
    # sorts the values in a list using in-order traversal
    print(numbers_tree.search(20))  # True
    print(numbers_tree.search(200))  # False
