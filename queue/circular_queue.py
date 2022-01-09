class Queue:
    def __init__(self, size):
        self.items = size * [None]
        self.size = size
        self.start = -1
        self.top = -1

    def __str__(self):
        return " ".join([str(i) for i in self.items])

    def enqueue(self, value):
        if self.is_full():
            return "The queue is full"
        else:
            if self.top + 1 == self.size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of the queue."

    def dequeue(self):
        if self.is_empty():
            return "The queue is empty!"
        first_element = self.items[self.start]
        start = self.start
        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif self.start + 1 == self.size:
            self.start = 0
        else:
            self.start += 1
        self.items[start] = None
        return first_element

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.size:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return "The queue is empty!"
        return self.items[self.start]

    def delete_queue(self):
        self.items = self.size * [None]
        self.top = -1
        self.start = -1


if __name__ == "__main__":
    pass
