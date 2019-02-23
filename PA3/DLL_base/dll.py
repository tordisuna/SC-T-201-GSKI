
class Node:
    def __init__(self, element=None, prev=None, next=None):
        self.element = element
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self, *args, **kwargs):
        self._header = Node()
        self._trailer = Node(None, self._header)
        self._header.next = self._trailer
        self.__size = 0
        self.__current = self._trailer  # For iteration
        self.__rev_current = self._header  # used when reversed
        self.__current_position = 1
        self.__rev_position = 0
        self.__reversed = False

    def _insert_between(self, element, node_a, node_b):
        new_node = Node(element, node_a, node_b)
        if self.__reversed:
            new_node.next = node_a
            new_node.prev = node_b
            node_a.prev = node_b.next = new_node
        else:
            node_b.prev = node_a.next = new_node
        self.__size += 1
        return new_node

    def _delete_node(self, node, position):
        node.prev.next, node.next.prev = node.next, node.prev
        if position <= self.__current_position:
            self.__current_position -= 1
        if position < self.__rev_position:
            self.__rev_position -= 1
        self.__size -= 1
        if node is self.__current:
            self.move_to_next()
        else:
            self._correct_rev()
        return node.element

    def is_empty(self):
        return self.__size == 0

    def get_size(self):
        return self.__size

    def _swap(self, node_1, node_2):
        '''Swap contents of 2 nodes'''
        node_1.element, node_2.element = node_2.element, node_1.element

    def _insertion_sort(self):
        if self.get_size() < 2:
            return  # List of len < 2 is already sorted
        pivot = self._get_next(self._first)
        while pivot is not self._get_next(self._last):
            swap = pivot
            while swap is not self._first:
                next_node = self._get_prev(swap)
                if next_node.element > swap.element:
                    self._swap(swap, next_node)
                else:
                    break
                swap = next_node
            pivot = self._get_next(pivot)

    # To ease use with reversed, I only use these functions when dealing
    # with node positioning.

    @property
    def _first(self):
        '''Get first proper node'''
        if self.__reversed:
            return self._trailer.prev
        return self._header.next

    @property
    def _last(self):
        '''Get last proper node'''
        if self.__reversed:
            return self._header.next
        return self._trailer.prev

    def _get_next(self, node):
        '''Get node that follows given node'''
        if self.__reversed:
            return node.prev
        return node.next

    def _get_prev(self, node):
        '''Get node that precedes given node'''
        if self.__reversed:
            return node.next
        return node.prev

    # Required functions

    def __str__(self):
        string = ""
        if self.is_empty():
            return string
        node = self._first
        while node is not self._get_next(self._last):
            string += str(node.element) + " "
            node = self._get_next(node)
        return string

    def __len__(self):
        return self.get_size()

    def insert(self, element):
        self._insert_between(
            element, self._get_prev(self.__current), self.__current
        )
        if self.__rev_position >= self.__current_position:
            self.__rev_position += 1
        self.__current_position += 1
        self.move_to_prev()

    def remove(self):
        if self.__current is not self._get_next(self._last):
            val = self._delete_node(self.__current, self.__current_position)
            return val

    def get_value(self):
        return self.__current.element

    def move_to_next(self):
        if self.__current is not self._get_next(self._last):
            self.__current = self._get_next(self.__current)
            self.__current_position += 1
            self._correct_rev()

    def move_to_prev(self):
        if self.__current is not self._first:
            self.__current = self._get_prev(self.__current)
            self.__current_position -= 1
            self._correct_rev()

    def move_to_pos(self, position: int):
        if 0 <= position <= self.get_size():
            diff = position - self.__current_position + 1
            for _ in range(diff):
                self.move_to_next()
            for _ in range(-diff):
                self.move_to_prev()

    def _correct_rev(self):
        '''nudges self.__rev_current by 1 if necessary'''
        expected_pos = (self.get_size() + 1) - self.__current_position
        diff = self.__rev_position - expected_pos
        if diff < 0:
            self.__rev_current = self._get_next(self.__rev_current)
            self.__rev_position += 1
        elif diff > 0:
            self.__rev_current = self._get_prev(self.__rev_current)
            self.__rev_position -= 1

    def _reset_current(self):
        self.__current_position = 1
        self.__rev_position = self.__size
        self.__current = self._first
        self.__rev_current = self._last

    def remove_all(self, value):
        node = self._last
        reset = False
        for i in range(self.get_size(), 0, -1):
            if node.element == value:
                if node is self.__current:
                    reset = True
                self._delete_node(node, i)
                if node is self.__rev_current:
                    self.__rev_current = self._get_next(
                        self._get_prev(self.__rev_current))
            node = self._get_prev(node)
        if reset:
            self._reset_current()

    def reverse(self):  # O(1)
        self.__reversed = not self.__reversed
        self.__current, self.__rev_current = self.__rev_current, self.__current

    def sort(self):
        self._insertion_sort()
        self._reset_current()
