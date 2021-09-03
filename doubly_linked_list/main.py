class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if location == 0:
                node.next = self.head
                self.head.prev = node
                self.head = node
            elif location == -1:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                index = 0
                pointer = self.head
                while index < location - 1:
                    pointer = pointer.next
                    index += 1
                node.next = pointer.next
                node.prev = pointer
                node.next.prev = node
                pointer.next = node

    def traverse(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            pointer = self.head
            while pointer:
                if pointer.next is None:
                    print(pointer.value)
                else:
                    print(pointer.value, end="->")
                pointer = pointer.next


if __name__ == "__main__":
    d = DoublyLinkedList()

    print([node.value for node in d])
    d.insert(5, 0)
    d.insert(0, 0)
    d.insert(2, 1)
    d.insert(6, 2)
    print([node.value for node in d])
    d.traverse()
