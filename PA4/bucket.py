from sll import LinkedList


class ItemExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Bucket(LinkedList):
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
        for item in self:
            if item.next is not None and item.next.element.key == key:
                self._delete_node(item.next, item)
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
