class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        pointer = self.head
        while pointer:
            yield pointer
            pointer = pointer.next


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(item.value) for item in self.linked_list]
        return "\n".join(values)

    def is_empty(self):
        """ If linked list's head is None, So it's empty. """
        return self.linked_list.head is None

    def push(self, value):
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def pop(self):
        if self.is_empty():
            return "The stack is empty"
        node_value = self.linked_list.head.value
        self.linked_list.head = self.linked_list.head.next
        return node_value

    def peak(self):
        if self.is_empty():
            return "The stack is empty"
        return self.linked_list.head.value

    def delete_stack(self):
        self.linked_list.head = None


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print("Head is: ", stack.peak())
    print("----------POP-----------")
    stack.pop()
    print(stack)
    print("Head is: ", stack.peak())

    print("----------Delete the stack-----------")
    stack.delete_stack()
    print(stack)
