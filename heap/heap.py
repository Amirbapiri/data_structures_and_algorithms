"""
# priority queue: is a list whose deletions and access are just like
classic queue, but whose insertions are ordered array. We only delete
and access data from the front of the priority queue, but when we insert
data, we always make sure the data remains sorted in a specific order.
# priority queue is an abstract data structure, which means it can be
implemented using other data structures. We use ordered array.
# Ordered array:
    - Has two primary operations: deletions and insertions
    - We can tweak our implemention so that we consider
        the 'end' of array as the 'front' of the priority queue so
        we can always delete from the end of the array which is
        possible in O(1).
        our array-based priority queue, then, has deletion in O(1)
        and insertion as O(N), oops!
        IS THERE ANY OTHER OPTION TO PREVENT INSERTION IN O(N)?
        YEEEEEESSSS ^_^
        Say hi to 'HEAPS'.
# Heaps:
    - There are several different types of heaps.
    - The binary heap is a specific type of binary tree.
        - as we may know, binary tree is a kind of tree which each 
            node has a maximum of two child nodes.
    - Even binary heaps come in two flavors: Max-Heap and Min-Heap
    - The heap is a binary tree that holds the following conditions:
        - The value of each node must be greater than each of its
            descendant nodes (heap condition).
        - The tree must be complete.
            - complete tree:
                Is a tree that is completely filled with nodes; no nodes
                are missing. So, if you read each level of the tree from
                left to right, all of the nodes are there.
                However, the bottom row can have empty positions as long as
                aren't any nodes to the right of these empty positions.
    - Focusing on Max-Heap:
        - The root node, will always have the greatest value.
            (It's smallest value in Min-Heap.)
    - Has two primary operations: inserting and deleting
            
    - Common operations on Binary Heap:
        - Creation of Binary Heap
        - Peek top of Binary Heap
        - Extract Min / Extract Max 
        - Traversal of Binary Heap
        - Size of Binary Heap
        - Insert value in Binary Heap
        - Delete the entire Binary heap
    
    - Implemention Options
        - Array Implementation
            Insertion:
                left child: cell[2x]
                right child: cell[2x + 1]
        - Reference / Pointer Implementation

"""

class Heap:
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1
    
    def peak(self):
        if self.heap_size:
            return self.custom_list[1]
        return "Heap is empty"
    
    def size_of_heap(self):
        if self.heap_size:
            return self.heap_size
        return "Heap is empty"
    
    def level_order_traversal(self):
        if self.heap_size:
            for i in range(1, self.heap_size + 1):
                print(self.custom_list[i])
        return "Heap is empty"


def peak(root_node):
    if not root_node:
        return
    return root_node.custom_list[1]

def size_of_heap(root_node):
    if not root_node:
        return
    return root_node.heap_size


if __name__ == "__main__":
    h = Heap(5)
    print(h.custom_list)