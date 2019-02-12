from dll import DoublyLinkedList


class DLL_PosList(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self._current_node = self._trailer

    def insert(self, element):
        current = self._current_node
        new_node = self._insert_between(element, current.prev, current)
        self._current_node = new_node

    def move_to_next(self):
        if self._current_node is not self._trailer:
            self._current_node = self._current_node.next

    def move_to_prev(self):
        if self._current_node.prev is not self._header:
            self._current_node = self._current_node.prev

    def get_value(self):
        return self._current_node.element

    def remove(self):
        if self._current_node is not self._trailer:
            self._delete_node(self._current_node)
            self._current_node = self._current_node.next

if __name__ == "__main__":
    lis = DLL_PosList()
    lis.insert("A")
    lis.insert("B")
    lis.insert("C")
    print(lis)
    lis.print_reversed()

    print(lis)
    lis.remove()
    print(lis)
    lis.remove()
    print(lis)

    lis = DLL_PosList()
    lis.insert('A')
    lis.insert('B')
    lis.move_to_next()
    lis.insert('C')
    lis.move_to_prev()
    lis.insert('D')
    print(lis)
