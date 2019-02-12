from node import Node


class LinkedList(object):
    def __init__(self):
        self.front = None
        self.back = self.front
        self.size = 0

    def push_back(self, value):
        new_back = Node(value)
        if self.back is None:
            self.back = self.front = new_back
        self.back.next = new_back
        self.back = new_back
        self.size += 1

    def pop_front(self):
        if self.front is not None:
            value = self.front.value
            self.front = self.front.next
            self.size -= 1
            return value

    def push_front(self, value):
        new_front = Node(value, self.front)
        self.front = new_front
        self.size += 1

    def pop_back(self):
        if self.front is None:
            return
        if self.front.next is None:
            value = self.front.value
            self.front = self.back = None
            self.size = 0
            return value
        current_node = self.front
        while current_node.next.next is not None:
            current_node = current_node.next
        value = current_node.next.value
        current_node.next = None
        self.back = current_node
        self.size -= 1
        return value

    def get_size(self):
        return self.size


if __name__ == "__main__":
    my_ll = LinkedList()
    for i in range(10):
        my_ll.push_back(i)
    while my_ll.get_size():
        print(my_ll.pop_back())
