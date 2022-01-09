class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        pointer = self.head
        while pointer:
            yield pointer
            pointer = pointer.next


class Queue:
    """
    Queue can also be implemented using linked list.
    'Time complexity' of the defined functionalities using linked list,
    is O(1). 'Space complexity' is also O(1)
    """

    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        return " ".join([str(value) for value in self.linked_list])

    def is_empty(self):
        return self.linked_list.head is None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            """
            # the queue is empty, both head and tail point 
            to the same node.
            in case of enqueue, we always add the new value to the end of
            the list and then we modify the tail to point to the
            new value.
            """
            self.linked_list.head = node
            self.linked_list.tail = node
            return "Element inserted."
        self.linked_list.tail.next = node
        self.linked_list.tail = node
        return "Element inserted."

    def dequeue(self):
        """
        In case of dequeue, we remove the first element which head
        is pointing to. Then, we set the head to point to the
        next value of the list.
        """
        if self.is_empty():
            return "The queue is empty."
        temp = self.linked_list.head
        if self.linked_list.head == self.linked_list.tail:
            self.linked_list.head = None
            self.linked_list.tail = None
        else:
            self.linked_list.head = self.linked_list.head.next
        return temp

    def peek(self):
        if self.is_empty():
            return "The queue is empty."
        return self.linked_list.head

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None
