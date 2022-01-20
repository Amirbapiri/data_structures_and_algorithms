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
from enum import Enum


class HeapType(Enum):
    MIN_HEAP = "MIN_HEAP",
    MAX_HEAP = "MAX_HEAP"


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

    def adjust(self, index, heap_type, node=None):
        parent_index = int(index / 2)
        if index <= 1:
            return
        if heap_type == HeapType.MIN_HEAP:
            if self.custom_list[index] < self.custom_list[parent_index]:
                self.custom_list[index], self.custom_list[parent_index] = self.custom_list[parent_index], self.custom_list[index]
            self.adjust(
                index=parent_index,
                node=self.custom_list[index],
                heap_type=heap_type
            )
        elif heap_type == HeapType.MAX_HEAP:
            if self.custom_list[index] > self.custom_list[parent_index]:
                self.custom_list[index], self.custom_list[parent_index] = self.custom_list[parent_index], self.custom_list[index]
            self.adjust(
                index=parent_index,
                node=self.custom_list[index],
                heap_type=heap_type
            )
        else:
            return None

    def insert(self, value, heap_type):
        """
        # Time complexity: O(LogN)
        # Space complexity: O(LogN)
        """
        if (self.heap_size + 1) == self.max_size:
            return "The binary heap is full"
        self.custom_list[self.heap_size + 1] = value
        self.heap_size += 1

        # put the new value to it's proper position
        self.adjust(index=self.heap_size, heap_type=heap_type)
        return "The value has been inserted."


if __name__ == "__main__":
    h = Heap(5)
    print(h.custom_list)
    h.insert(4, HeapType.MAX_HEAP)
    print(h.custom_list)
    h.insert(5, HeapType.MAX_HEAP)
    print(h.custom_list)
    h.insert(2, HeapType.MAX_HEAP)
    print(h.custom_list)
    h.insert(1, HeapType.MAX_HEAP)
    print(h.custom_list)

    h.level_order_traversal()
