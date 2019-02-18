class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.front = None
        self.back = self.front
        self.size = 0

    def push_front(self, value):
        new_front = Node(value, self.front)
        self.front = new_front
        self.size += 1

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

    def get_size(self):
        return self.size

    def __str__(self):
        string = ""
        node = self.front
        if node is None:
            return string
        while node.next is not None:
            string += str(node.value) + " "
            node = node.next
        return string + str(node.value)
