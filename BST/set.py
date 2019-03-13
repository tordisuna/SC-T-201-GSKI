class BSTNode(object):
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.element == other.element
        return self.element == other

    def __gt__(self, other):
        if isinstance(other, type(self)):
            return self.element > other.element
        return self.element > other

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.element < other.element
        return self.element < other


class MySet(object):
    def __init__(self, *args, **kwargs):
        self.root = None
        self.size = 0

    def add(self, value):
        self.size += 1
        if self.root is None:
            self.root = BSTNode(value)
            return
        self.add_recur(self.root, value)

    def add_recur(self, node, value):
        if value > node:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self.add_recur(node.right, value)
        elif value < node:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self.add_recur(node.left, value)
        else:
            self.size -= 1

    def contains(self, value):
        node = self.root
        while node is not None:
            if node == value:
                return True
            elif node > value:
                node = node.left
            else:
                node = node.right
        return False

    def __str__(self):
        return self.inorder_string(self.root)

    def inorder_string(self, node):
        if node is None:
            return ""
        string = self.inorder_string(node.left)
        if string:
            string += " "
        string += str(node.element)
        right_str = self.inorder_string(node.right)
        if right_str:
            string += " " + right_str
        return string

    def __contains__(self, value):
        return self.contains(value)

    def __len__(self):
        return self.size


if __name__ == "__main__":
    my_set = MySet()
    my_set.add(1)
    my_set.add(6)
    my_set.add(3)
    my_set.add(4)
    my_set.add(5)
    my_set.add(7)
    my_set.add(2)
    print(my_set)
    print(2 in my_set)
    print(1 in my_set)
    print(3 in my_set)
    print(4 in my_set)
    print(5 in my_set)
    print(len(my_set))
    from random import randint
    for i in range(40):
        my_set.add(randint(0, 1000))
    print(len(my_set))
    print(my_set)
