"""
A non-linear data structure with hierarchical relationships amount its elements
without any cycle.

* Properties:
    -- Represents hierarchical data
    -- Each node has two components: 1: Data, 2: link to its sub category
* Why do we use it:
    -- Quicker and easier access to the data
    -- Store hierarchical data(folder structure, organization structure, XML/HTML).
    -- verity of tries in case of having better performance of doing different functionalities
        -- BST, AVL, Red Black Tree, Trie
"""


class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = "    " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, node):
        self.children.append(node)


if __name__ == "__main__":
    tree = TreeNode('Drinks', [])
    cold = TreeNode('Cold', [])
    hot = TreeNode('Hot', [])

    tree.add_child(cold)
    tree.add_child(hot)

    tea = TreeNode('Tee', [])
    coffee = TreeNode('Coffee', [])
    soda = TreeNode('Soda', [])
    water = TreeNode('Water', [])

    cold.add_child(soda)
    cold.add_child(water)

    hot.add_child(tea)
    hot.add_child(coffee)

    print(tree)
