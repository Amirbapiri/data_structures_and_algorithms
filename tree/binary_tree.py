"""
Binary tree can be represented in two ways:
    -- Linked list
    -- Python List (array)
        ---- Left child -> cell[2x]
        ---- Right child -> cell[2x + 1]
            ----- we don't use the first index which is 0
            ----- x is the location of root node of the tree
            ----- root always takes the first cell of the array
    -- Operations:
        ---- Creation of tree
        ---- Insertion of a node
        ---- Deletion of a node
        ---- Search for a value
        ---- Traverse all nodes
            ------ Depth first search [Pre-order, In-order, post-order]
            ------ Breadth first search [level order]
        ---- Deletion of tree
"""
from enum import Enum


class TraversingTypes(Enum):
    PRE_ORDER = "pre_order"
    IN_ORDER = "in_order"
    POST_ORDER = "post_order"
    LEVEL_ORDER = "level_order"


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traverse_type):
        if traverse_type == TraversingTypes.PRE_ORDER:
            return self._pre_order(self.root)
        elif traverse_type == TraversingTypes.IN_ORDER:
            return self._in_order(self.root)
        elif traverse_type == TraversingTypes.POST_ORDER:
            return self._post_order(self.root)

    def _pre_order(self, start, traversal=""):
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self._pre_order(start.left, traversal)
            traversal = self._pre_order(start.right, traversal)
        return traversal

    def _in_order(self, start, traversal=""):
        """Left->Root->Right"""
        if start:
            traversal = self._in_order(start.left, traversal)
            traversal += (str(start.value) + " - ")
            traversal = self._in_order(start.right, traversal)
        return traversal

    def _post_order(self, start, traversal=""):
        """Left->Right->Root"""
        if start:
            traversal = self._post_order(start.left, traversal)
            traversal = self._post_order(start.right, traversal)
            traversal += (str(start.value) + " - ")
        return traversal


if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    pre_order_result = tree.print_tree(TraversingTypes.PRE_ORDER)
    print("pre order: ", pre_order_result)
    in_order_result = tree.print_tree(TraversingTypes.IN_ORDER)
    print("in order: ", in_order_result)
    post_order_result = tree.print_tree(TraversingTypes.POST_ORDER)
    print("post order: ", post_order_result)
