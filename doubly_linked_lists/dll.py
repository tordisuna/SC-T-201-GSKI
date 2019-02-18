from node import Node


class DoublyLinkedList():
    def __init__(self, *args, **kwargs):
        self._header = Node()
        self._trailer = Node(None, self._header)
        self._header.next = self._trailer
        self.__size = 0
        self.__current = self._header  # For iteration

    def _insert_between(self, element, node_a, node_b):
        new_node = Node(element, node_a, node_b)
        node_a.next = new_node
        node_b.prev = new_node
        self.__size += 1
        return new_node

    def _delete_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        self.__size -= 1
        return node.element

    def is_empty(self):
        return self.__size == 0

    def get_size(self):
        return self.__size

    def _get_head_node(self):
        return self._header.next

    def _get_tail_node(self):
        return self._trailer.prev

    @property
    def _first(self):
        return self._header.next

    @property
    def _last(self):
        return self._trailer.prev

    def __str__(self):
        string = ""
        if self.is_empty():
            return string
        node = self._header.next
        while node.next is not self._trailer:
            string += str(node.element) + " "
            node = node.next
        return string + str(node.element)

    def __len__(self):
        return self.get_size()

    def print_reversed(self):
        if self.is_empty():
            print()
            return
        node = self._trailer.prev
        while node.prev is not self._header:
            print(node.element, end=" ")
            node = node.prev
        print(node.element)

    def _get_node(self, element):
        '''Get the first node with the specified element. Raises LookupError
        if not found. O(n)
        '''
        node = self._header.next
        while node is not self._trailer:
            if node.element == element:
                return node
            node = node.next
        raise LookupError()

    def _copy(self):
        '''Copy all values into a new dll-type'''
        new_dll = type(self)()  # creates a new dll or inherited type
        for element in self:
            new_dll._insert_between(
                element, new_dll._trailer.prev, new_dll._trailer
            )
        return new_dll

    def __iter__(self):
        self.__current = self._first
        return self

    def __next__(self):
        if self.__current is not self._trailer:
            self.__current = self.__current.next
            return self.__current.prev.element
        raise StopIteration()

    def swap_node(self, node_1, node_2):
        '''Swaps entire nodes in the dll. Not just the contents'''
        node_1.next, node_2.next = node_2.next, node_1.next
        node_1.prev, node_2.prev = node_2.prev, node_1.prev
        node_1.next.prev, node_2.next.prev = node_1, node_2
        node_1.prev.next, node_2.prev.next = node_1, node_2

    def swap(self, node_1, node_2):
        '''Swap contents of 2 nodes'''
        node_1.element, node_2.element = node_2.element, node_1.element

    def ordered_insert(self, element):
        for my_element in self:
            if my_element >= element:
                node = self.__current.prev
                return self._insert_between(element, node.prev, node)
        self._insert_between(element, self._trailer.prev, self._trailer)

    def insertion_sort(self):
        if len(self) < 2:
            return
        node = self._first.next
        while node is not self._trailer:
            comparison_node = node.prev
            while comparison_node is not self._header:
                if node.element > comparison_node.element:
                    self.swap(node, comparison_node.next)
                    break
                comparison_node = comparison_node.prev
            node = node.next


def printReverse(doubly_linked_list):  # O(n^2)
    for i in range(len(doubly_linked_list) - 1, -1, -1):
        node = doubly_linked_list._first
        for _ in range(i):
            node = node.next
        print(node.element, end=' ')


if __name__ == "__main__":
    my_dll = DoublyLinkedList()
    for i in range(10, 0, -1):
        my_dll.ordered_insert(i)
    print(my_dll)
    printReverse(my_dll)
