from dll import DoublyLinkedList


class DLL_Set(DoublyLinkedList):
    def add(self, element):
        if element not in self:
            self._insert_between(element, self._header, self._header.next)

    def remove(self, element):
        try:
            node = self._get_node(element)
            self._delete_node(node)
            return node
        except LookupError:
            pass

    def __contains__(self, element):
        try:
            self._get_node(element)
            return True
        except LookupError:
            return False

    def __add__(self, other):
        new_set = self._copy()
        for element in other:
            new_set.add(element)
        return new_set

    def __mul__(self, other):
        new_set = other._copy()
        for element in new_set:
            if element not in self:
                new_set.remove(element)
        return new_set

    def __sub__(self, other):
        new_set = self._copy()
        for element in other:
            new_set.remove(element)
        return new_set

    def subset(self, other):
        '''Returns true if other is a subset of self else false'''
        for element in other:
            if element not in self:
                return False
        return True

    def __eq__(self, other):
        return self.subset(other) and other.subset(self)


if __name__ == "__main__":
    my_set = DLL_Set()
    for i in range(10):
        my_set.add(i)
    print(my_set)
    for i in range(20):
        my_set.add(i)
    print(my_set)
    if 10 in my_set:
        print("10 is in the set")

    my_other_set = DLL_Set()
    for i in range(10, 25):
        my_other_set.add(i)

    union = my_set + my_other_set
    print(union)
    intersection = my_set * my_other_set
    print(intersection)
    difference = my_set - my_other_set
    print(difference)

    set1 = my_set._copy()
    set2 = my_set._copy()
    print(set1 == set2)