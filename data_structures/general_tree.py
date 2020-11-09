"""
Implementation of general tree

"""


class TreeNode:
    """
    General Tree class.
    """
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        """
        Add child node into the tree.
        """
        child.parent = self  # child is instance of TreeNode and its parent is the instance 'self'
        self.children.append(child)

    def get_level(self):
        """
        Get the level of the node. Count ancestor.
        """
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""  # if no parent no prefix needed
        print(prefix + self.data)
        # go through each tree and print the children
        if self.children:
            for child in self.children:
                child.print_tree()  # use recursion


def build_product_tree():
    root = TreeNode("Stock Market")

    tech_stock = TreeNode("Tech Stocks")
    tech_stock.add_child(TreeNode("Apple"))  # the parent of TreeNode("Apple") becomes the root tree "Tech Stock"
    tech_stock.add_child(TreeNode("Amazon"))
    tech_stock.add_child(TreeNode("Google"))
    tech_stock.add_child(TreeNode("Microsoft"))

    funds = TreeNode("ETFs")
    funds.add_child(TreeNode("LIT"))
    funds.add_child(TreeNode("ICLN"))
    funds.add_child(TreeNode("QQQ"))
    funds.add_child(TreeNode("SPY"))

    non_tech_stock = TreeNode("Non Tech Stocks")
    non_tech_stock.add_child(TreeNode("Coca Cola"))
    non_tech_stock.add_child(TreeNode("Starbucks"))

    root.add_child(tech_stock)
    root.add_child(funds)
    root.add_child(non_tech_stock)

    return root


if __name__ == '__main__':
    stock_tree = build_product_tree()
    stock_tree.print_tree()
