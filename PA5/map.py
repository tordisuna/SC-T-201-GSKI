from dataclasses import dataclass, field


@dataclass(order=True)
class Item(object):
    key: object = field()
    value: object = field(compare=False)


@dataclass(order=True)
class BSTNode(object):
    element: object = field()
    left: object = field(default=None, compare=False)
    right: object = field(default=None, compare=False)


class MySet(object):
    def __init__(self, *args, **kwargs):
        self.root = None
        self.size = 0

    def add(self, key, value):
        self.size += 1
        if self.root is None:
            self.root = BSTNode(Item(key, value))
            return
        self.add_recur(self.root, Item(key, value))

    def add_recur(self, node, item):
        if item > node.element:
            if node.right is None:
                node.right = BSTNode(item)
            else:
                self.add_recur(node.right, item)
        elif item < node.element:
            if node.left is None:
                node.left = BSTNode(item)
            else:
                self.add_recur(node.left, item)
        else:
            self.size -= 1

    def contains(self, key):
        node = self.root
        while node is not None:
            if node.element.key == key:
                return True
            elif node.element.key > key:
                node = node.left
            else:
                node = node.right
        return False

    def __str__(self):
        return " ".join(map(str, self.inorder()))

    def __contains__(self, value):
        return self.contains(value)

    def __len__(self):
        return self.size

    def remove(self, key):
        self.size -= 1
        self.root = self.__rem(key, self.root)

    def __rem(self, key, node):
        if node is None:
            self.size += 1  # Not found
        elif node.element.key > key:
            node.left = self.__rem(key, node.left)
        elif key > node.element.key:
            node.right = self.__rem(key, node.right)
        else:
            node = self.__remove_node(node)
        return node

    def __remove_node(self, node):
        if node.left is None or node.right is None:
            return node.left or node.right
        leftmost = self.__leftmost(node.right)
        node.element = leftmost.element
        node.right = self.__rem(leftmost.element, node.right)
        return node

    def __leftmost(self, node):
        """Find leftmost node in subtree of given node."""
        if node.left:
            return self.__leftmost(node.left)
        return node

    def __rightmost(self, node):
        """Find rightmost node in subtree of given node."""
        if node.right:
            return self.__rightmost(node.right)
        return node

    def min(self):
        return self.__leftmost(self.root).element

    def max(self):
        return self.__rightmost(self.root).element

    def search(self, prefix):
        matching = list()
        self.__find_prefix(self.root, prefix, matching)
        return matching

    def __find_prefix(self, node, prefix, matching):
        if node is None:
            return None  # Not found
        elif node.element.find(prefix) == 0:
            matching.append(node.element)
            self.__find_prefix(node.left, prefix, matching)
            self.__find_prefix(node.right, prefix, matching)
        else:
            if node > prefix:
                self.__find_prefix(node.left, prefix, matching)
            elif prefix > node:
                self.__find_prefix(node.right, prefix, matching)

    def inorder(self):
        for node in self.__inorder_subtree(self.root):
            yield node.element

    def __inorder_subtree(self, node):
        if node is not None:
            for l_node in self.__inorder_subtree(node.left):
                yield l_node
            yield node
            for r_node in self.__inorder_subtree(node.right):
                yield r_node

    def __iter__(self):
        return self.inorder()

    def print_range(self, min, max):
        return self.__print_range(self.root, min, max)

    def __print_range(self, node, lo, hi):
        if node is None:
            return
        if node.element.key >= lo:
            self.__print_range(node.left, lo, hi)
        if lo <= node.element.key <= hi:
            print(node.element)
        if node.element.key <= hi:
            self.__print_range(node.right, lo, hi)


if __name__ == "__main__":
    my_set = MySet()
    my_set.add(1, "asd")
    my_set.add(6, 6)
    my_set.add(3, 3)
    my_set.add(4, 4)
    my_set.add(5, 5)
    my_set.add(7, 7)
    my_set.add(2, 2)
    print(my_set)
    print(2 in my_set)
    print(1 in my_set)
    print(3 in my_set)
    print(4 in my_set)
    print(5 in my_set)
    print(len(my_set))
    from random import randint
    for i in range(20):
        my_set.add(randint(0, 1000), i)
    my_set.add(500, "wow")
    for i in range(20):
        my_set.add(randint(0, 1000), i * 5)

    print(len(my_set))
    print(my_set)
    my_set.remove(54)
    my_set.remove(999)
    my_set.remove(998)
    my_set.remove(997)
    my_set.remove(500)
    my_set.remove(501)
    print(len(my_set))
    print(my_set)
    # print(my_set.min())
    # print(my_set.max())
    # my_set = MySet()
    # my_set.add("fake news")
    # my_set.add("gratuity")
    # my_set.add("wow")
    # my_set.add("grades")
    # my_set.add("grandmaster flash")
    # my_set.add("ananas")
    # print(my_set.search("gra"))
    # print([a for a in my_set.inorder()])
    # print(my_set)
    my_set.add(50, "fiddy")
    my_set.print_range(3, 50)
