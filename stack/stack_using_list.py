"""
Stack operations are:
    - Create Stack
    - Push
    - Pop
    - Peek
    - is_empty
    - is_full (If limitation has considered)
    - delete_stack

    * Stack creation:
        - using List
            -- Easy to implement
            -- Speed problem when it grows
        - using Linked list
            -- Fast performance
            -- Implementation is not easy
"""


class Stack:
    """
    Implementing using List
    """

    def __init__(self):
        self.list = []

    def __str__(self):
        items = [str(x) for x in reversed(self.list)]
        return "\n".join(items)

    def is_empty(self):
        return not len(self.list)

    def push(self, value):
        self.list.append(value)
        return "The element appended."

    def pop(self):
        if self.is_empty():
            return "The stack is empty"
        return self.list.pop()

    def peak(self):
        if self.is_empty():
            return "The stack is empty"
        return self.list[-1]

    def erase(self):
        self.list = []


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    # print("-------POP-------")
    # stack.pop()
    # print(stack)

    print(stack.peak())
    stack.erase()
    print(stack)
