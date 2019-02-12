from node import Node


class DoublyLinkedList():
    def __init__(self, *args, **kwargs):
        self._header = Node()
        self._trailer = Node(None, self._header)
        self._header.next = self._trailer
        self.__size = 0

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

    def __str__(self):
        string = ""
        if self.is_empty():
            return string
        node = self._header.next
        while node.next is not self._trailer:
            string += str(node.element) + " "
            node = node.next
        return string + str(node.element)

    def print_reversed(self):
        if self.is_empty():
            print()
            return
        node = self._trailer.prev
        while node.prev is not self._header:
            print(node.element, end=" ")
            node = node.prev
        print(node.element)
