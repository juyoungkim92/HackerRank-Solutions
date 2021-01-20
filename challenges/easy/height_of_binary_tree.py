"""
https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

Complete the getHeight or height function in the editor. It must return the height of a binary tree as an integer.

"""

# Setup classes for Tree


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is not None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root):
    """
    Method to determine the height of a given binary tree.

    Explanation:

    1. Check if given root node is None. If only 1 node, root is not None so return max(left, right) + 1
    2. If root not None, recursively run height with left and right root.
    3. Left and Right roots are None (for given 1 node tree). Thus, return -1
    4. Max(-1, -1) is -1 and +1 is 0.
    5. Therefore height h = 0 for a single node binary tree.
    """
    if root is None:
        return -1

    return max(height(root.left), height(root.right)) + 1
