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

    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        items = [str(x) for x in reversed(self.list)]
        return "\n".join(items)

    def is_empty(self):
        return not len(self.list)

    def is_full(self):
        return len(self.list) == self.max_size

    def push(self, value):
        if not self.is_full():
            self.list.append(value)
            return "The item appended."
        return "Stack is full."

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

    def delete_stack(self):
        self.list = None


if __name__ == "__main__":
    stack = Stack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    # Stack is full
    print(stack.push(4))  # Stack is full.
    print(stack.is_empty(), stack.is_full())
    print(stack.peak())
    print(stack.pop())
    print(stack.peak())
