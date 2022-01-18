"""
Binary search tree (BST) is a node-based binary tree
with the following properties:
    - In the left subtree, the value of a node is less than or equal
    to its parent node's value.
    - In the right subtree, the value of a node is greater than its
    parent node's value.
    - The left and right subtree each must also be a binary search tree.

# Operations:
    - Creation of Tree
    - Insertion of a node
    - Deletion of a node
    - Search for a value
    - Traverse all nodes
    - Deletion of a node
"""


class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


def insert(value, root):
    # Time complexity: O(logN)
    # Space complexity: O(logN)
    if root.value is None:
        root.value = value
    elif value <= root.value:
        if root.left_child is None:
            root.left_child = BSTNode(value)
        else:
            insert(value, root.left_child)
    else:
        if root.right_child is None:
            root.right_child = BSTNode(value)
        else:
            insert(value, root.right_child)
    return "The node has been inserted!"


def pre_order_traversal(root):
    # Time complexity: O(n)
    if not root:
        return
    print(root.value)
    pre_order_traversal(root.left_child)
    pre_order_traversal(root.right_child)


def in_order_traversal(root):
    # Time complexity: O(n)
    # Space complexity: O(n)
    if not root:
        return
    in_order_traversal(root.left_child)
    print(root.value)
    in_order_traversal(root.right_child)


def post_order_traversal(root):
    if not root:
        return
    post_order_traversal(root.left_child)
    post_order_traversal(root.right_child)
    print(root.value)


def level_order_traversal(root):
    # TODO implement level order traversal.
    pass


def search(root, value):
    # Time complexity: O(logN)
    # Space complexity: O(logN)
    if root.value == value:
        return (True, root.value)
    if value <= root.value:
        if root.left_child.data == value:
            return (True, root.value)
        else:
            search(root.left_child, value)
    else:
        if root.right_child.data == value:
            return (True, root.value)
        else:
            search(root.right_child, value)
    return "Couldn't find the given value in the tree."


def delete(root):
    """
    In case of deletion a node in BST, we have three cases:
        #1 The node to be deleted is a leaf node (Doesn't have any children)
        #2 The node has on child
        #3 The node has two children
    """
    pass
