from sll import LinkedList


class ItemExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Node(object):
    def __init__(self, value=None, next=None):
        self.element = value
        self.next = next


class Bucket():
    def __init__(self):
        self.head = None
        self.back = self.head
        self.size = 0
        self.__current = None

    def pop_front(self):
        if self.head is not None:
            value = self.head.element
            self.head = self.head.next
            self.size -= 1
            return value

    def push_front(self, value):
        self.head = Node(value, self.head)
        self.size += 1

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

    def contains(self, key):
        return key in self

    def insert(self, key, data):
        if key in self:
            raise ItemExistsException()
        self.push_front(Item(key, data))

    def find(self, key):
        return self[key]

    def remove(self, key):
        if not self.is_empty() and self.head.element.key == key:
            self.pop_front()
            return
        for item in self:
            if item.next is not None and item.next.element.key == key:
                self._delete_node(item.next, item)
                return
        raise NotFoundException()

    def update(self, key, data):
        item = self.__get_full_item(key)
        item.value = data

    def __getitem__(self, key):
        item = self.__get_full_item(key)
        return item.value

    def __setitem__(self, key, data):
        try:
            self.__get_full_item(key).value = data
        except NotFoundException:
            self.push_front(Item(key, data))

    def __contains__(self, key):
        try:
            self.__get_full_item(key)
            return True
        except NotFoundException:
            return False

    def __get_full_item(self, key):
        '''Get the Item object where item.key = key'''
        for item in self:
            if item.element.key == key:
                return item.element
        raise NotFoundException()

    def _delete_node(self, node, prev_node):
        prev_node.next = node.next
        self.size -= 1
        return node.element