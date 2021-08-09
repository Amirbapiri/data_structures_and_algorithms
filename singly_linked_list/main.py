class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
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
                self.head = node
            elif location == -1:
                node.next = None
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
                    node.next = None
                    self.tail = node

    def traverse(self):
        if self.head is None:
            print("You have nothing to traverse dude!")
        else:
            pointer = self.head
            while pointer is not None:
                if pointer.next is None:
                    print(pointer.value)
                else:
                    print(pointer.value, end="->")
                pointer = pointer.next

    def search(self, value):
        if self.head is None:
            print("The list does not have any value.")
        else:
            pointer = self.head
            while pointer is not None:
                if pointer.value == value:
                    return pointer.value
                pointer = pointer.next
            return "Nothing found!"

    def delete(self, location):
        if self.head is None:
            print("The list does not have any value.")
        else:
            if location == 0:
                if self.head == self.tail:
                    # If so, they're pointing to the same value
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    # If so, they're pointing to the same value
                    self.head = None
                    self.tail = None
                else:
                    pointer = self.head
                    while pointer is not None:
                        # Moving pointer forward, right before the tail
                        if pointer.next == self.tail:
                            break
                        pointer = pointer.next
                    pointer.next = None
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
        """
        This method deletes entire list
        """
        if self.head is None:
            print("The list does not have any value.")
        else:
            self.head = None
            self.tail = None


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.insert(1, 1)
    singly_linked_list.insert(2, 0)
    singly_linked_list.insert(3, -1)
    singly_linked_list.insert(5, 1)
    singly_linked_list.insert(15, -1)
    singly_linked_list.insert(500, -1)
    singly_linked_list.insert(100, 0)
    singly_linked_list.insert(0, 0)
    print([node.value for node in singly_linked_list])
    #
    # singly_linked_list.traverse()
    # print(singly_linked_list.search(100))

    # Delete a node
    # singly_linked_list.delete(3)
    # print([node.value for node in singly_linked_list])
    # singly_linked_list.delete(-1)
    # print([node.value for node in singly_linked_list])
    # singly_linked_list.delete(2)
    # print([node.value for node in singly_linked_list])

    # Erase the linked list
    # singly_linked_list.erase()
    # print([node.value for node in singly_linked_list])
