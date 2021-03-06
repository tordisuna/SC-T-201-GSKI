from dll import DoublyLinkedList


class DLL_Deque(DoublyLinkedList):
    def add_front(self, element):
        self._insert_between(element, self._header, self._header.next)

    def add_back(self, element):
        self._insert_between(element, self._trailer.prev, self._trailer)

    def remove_front(self):
        if not self.is_empty():
            return self._delete_node(self._first)

    def remove_back(self):
        if not self.is_empty():
            return self._delete_node(self._last)

    def get_front(self):
        return self._first.element

    def get_back(self):
        return self._last.element


if __name__ == '__main__':
    queue = DLL_Deque()
    for i in range(10):
        queue.add_back(i)
    print(queue)
    queue.print_reversed()
    print(queue.get_size())

    for i in range(10):
        queue.add_front(i)
    for i in range(10):
        queue.remove_back()
    print(queue)
    queue.insertion_sort()
    print(queue)
