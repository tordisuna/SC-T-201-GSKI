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


class Bucket(object):
    def __init__(self):
        self.__head = None
        self.__size = 0
        self.__current = None  # For iteration only

    def insert(self, key, data):
        if key in self:
            raise ItemExistsException()
        self._push_front(Item(key, data))

    def update(self, key, data):
        item = self.__get_full_item(key)
        item.value = data

    def find(self, key):
        return self[key]

    def contains(self, key):
        return key in self

    def remove(self, key):
        if not self.is_empty() and self.__head.element.key == key:
            self._pop_front()
            return
        node = self.__head
        for i in range(self.__size - 1):
            if node.next.element.key == key:
                self._delete_node(node.next, node)
                return
            node = node.next
        raise NotFoundException()

    def __setitem__(self, key, data):
        try:
            self.__get_full_item(key).value = data
        except NotFoundException:
            self._push_front(Item(key, data))

    def __getitem__(self, key):
        '''Get the value associated with key'''
        item = self.__get_full_item(key)
        return item.value

    def __len__(self):
        return self.get_size()

    # Internal functions

    def __get_full_item(self, key):
        '''Get the item associated with key'''
        for item in self:
            if item.key == key:
                return item
        raise NotFoundException()

    def __contains__(self, key):
        try:
            self.__get_full_item(key)
            return True
        except NotFoundException:
            return False

    # Linked list functions

    def _pop_front(self):
        if not self.is_empty():
            self.__head = self.__head.next
            self.__size -= 1

    def _delete_node(self, node, prev_node):
        prev_node.next = node.next
        self.__size -= 1

    def _push_front(self, value):
        self.__head = Node(value, self.__head)
        self.__size += 1

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size <= 0

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        last = self.__current
        if last is None:
            raise StopIteration()
        self.__current = self.__current.next
        return last.element
