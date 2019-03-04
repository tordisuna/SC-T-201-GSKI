class Node(object):
    def __init__(self, value=None, next=None):
        self.element = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.back = self.head
        self.size = 0
        self.__current = None

    def push_back(self, value):
        new_back = Node(value)
        if self.back is None:
            self.back = self.head = new_back
        self.back.next = new_back
        self.back = new_back
        self.size += 1

    def pop_front(self):
        if self.head is not None:
            value = self.head.element
            self.head = self.head.next
            self.size -= 1
            return value

    def push_front(self, value):
        self.head = Node(value, self.head)
        self.size += 1

    def pop_back(self):
        if self.get_size() == 1:
            value = self.head.element
            self.front = self.back = None
            self.size = 0
            return value
        for node in self:
            if node.next is self.back:
                value = self._delete_node(node.next, node)
                self.back = node
                return value

    def _delete_node(self, node, prev_node):
        prev_node.next = node.next
        self.size -= 1
        return node.element

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size <= 0

    def __iter__(self):
        self.__current = self.head
        return self

    def __next__(self):
        last = self.__current
        if last is None:
            raise StopIteration()
        self.__current = self.__current.next
        return last

    def __len__(self):
        return self.get_size()
