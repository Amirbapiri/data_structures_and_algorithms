"""
# Queue is a data structure that stores items in First-In/First-Out manner.
# What we need Queue data structure?
    - Utilize first comming data first, while others wait for their turn
    - In general, any where you need to apply FIFO method.
        -- Printer queue
        -- Call center phone systems

- Queue operations are:
    - Create queue
    - Enqueue
    - Dequeue
    - Peek
    - isEmpty
    - isFull
    - deleteQueue


    * Queue creation:
        - using Python list
            -- Queue without capacity
            -- Queue with capacity (Circular Queue)
        - using Linked list
            -- Fast performance
            -- Implementation is not easy
"""


class Queue:
    FIRST_ELEMENT_INDEX = 0

    def __init__(self):
        self.items = []

    def __str__(self):
        return " ".join([str(i) for i in self.items])

    def enqueue(self, value):
        if value:
            self.items.append(value)
            return "The value is inserted at the end of the queue."

    def dequeue(self):
        """
        we remove elements from the beggining of the queue.
        """
        if self.is_empty():
            return "The queue is empty. No value to return!"
        return self.items.pop(self.FIRST_ELEMENT_INDEX)

    def peek(self):
        if not self.is_empty():
            return self.items[self.FIRST_ELEMENT_INDEX]
        return "The queue is empty. No 'peek' to be returned."

    def is_empty(self):
        if self.items:
            return len(self.items) == 0
        return "The queue is not initialized."

    def is_full(self):
        # If we want to have a circular queue (a queue with a limited size)
        pass

    def delete_queue(self):
        self.items = None


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    for i in range(10):
        q.enqueue(i)
    print(q.delete_queue())
    print(q.peek())
