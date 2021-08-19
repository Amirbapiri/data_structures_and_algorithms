class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def insert(self, value, location):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node
        else:
            if location == 0:
                node.next = self.head
                self.head = node
                self.tail.next = node
            elif location == -1:
                node.next = self.tail.next
                self.tail.next = node
                self.tail = node
            else:
                pointer = self.head
                index = 0
                while index < location - 1:
                    pointer = pointer.next
                    index += 1
                temp_node = pointer.next
                pointer.next = node
                node.next = temp_node
                if pointer == self.tail:
                    node.next = self.tail.next
                    self.tail = node
            return "Insertion done!"

    def traverse(self):
        if self.head is None:
            return "List is emtpy"
        else:
            pointer = self.head
            while pointer:
                if not pointer == self.tail:
                    print(pointer.value, end="->")
                else:
                    print(pointer.value)
                pointer = pointer.next
                if pointer == self.tail.next:
                    break

    def search(self, value):
        if self.head is None:
            print("The list does not have any value.")
        else:
            pointer = self.head
            while pointer:
                if pointer.value == value:
                    return pointer.value
                pointer = pointer.next
                if pointer == self.tail.next:
                    break
            return "Nothing found!"

    def delete(self, location):
        if self.head is None:
            print("The list does not have any value.")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    pointer = self.head
                    while pointer is not None:
                        if pointer.next == self.tail:
                            break
                        pointer = pointer.next
                    pointer.next = self.head
                    self.tail = pointer
            else:
                pointer = self.head
                index = 0
                while index < location - 1:
                    pointer = pointer.next
                    index += 1
                temp_node = pointer.next
                pointer.next = temp_node.next

    def erase(self):
        if self.head is None:
            print("The list does not have any value.")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None


if __name__ == "__main__":
    circular_linked_list = CircularLinkedList()
    circular_linked_list.insert(0, 0)
    circular_linked_list.insert(2, 0)
    circular_linked_list.insert(3, 1)
    circular_linked_list.insert(4, -1)
    circular_linked_list.insert(5, -1)
    circular_linked_list.insert(10, 0)
    circular_linked_list.insert(100, 3)

    circular_linked_list.traverse()
    circular_linked_list.insert(90, 3)
    circular_linked_list.traverse()

    # print(circular_linked_list.search(10))
    print([node.value for node in circular_linked_list])
    # circular_linked_list.delete(2)

    circular_linked_list.erase()
    print([node.value for node in circular_linked_list])
