from node import Node


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def add(self, value):
        new_tail = Node(value)
        if self.tail is None:
            self.tail = self.head = new_tail
        self.tail.next = new_tail
        self.tail = new_tail
        self.size += 1

    def remove(self):
        if self.head is not None:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value

    def get_size(self):
        return self.size


my_queue = Queue()
for i in range(100):
    my_queue.add(i)

print("Size: ", my_queue.get_size())

for _ in range(101):
    print(my_queue.remove())

print("Size: ", my_queue.get_size())
