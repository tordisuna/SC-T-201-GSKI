from dataclasses import dataclass, field


class Node(object):
    pass


@dataclass()
class Node(object):
    priority: object
    data: object = None
    parent: Node = None
    left: Node = None
    right: Node = None


class Heap(object):
    def __init__(self, *args, **kwargs):
        self.root = self.last_node = None

    def add(self, value, priority):
        if self.root is None:
            self.root = self.last_node = Node(priority, value)
            self.root.parent = Node(0, 0)
        elif self.last_node.parent.left is self.last_node:
            new_node = Node(priority, value, self.last_node.parent)
            self.last_node.parent.right = new_node
            self.last_node = new_node
        else:
            node = self.last_node
            while node.parent.right is node:
                node = node.parent
            if node is not self.root:
                node = node.parent.right
            while node.left is not None:
                node = node.left
            node.left = self.last_node = Node(priority, value, node)
        self._float_up(self.last_node)

    def remove(self):
        value = self.root.data
        self.root.data = self.last_node.data
        self.root.priority = self.last_node.priority
        node = self.last_node
        current = self.last_node
        if self.last_node is self.root:
            self.root = None
            return value
        elif node.parent.right is node:
            node = node.parent.left
        else:
            while node.parent.left is node:
                node = node.parent
            node = node.left
            while node.right is not None:
                node = node.right
        if current.parent.left is current:
            current.parent.left = None
        else:
            current.parent.right = None
        self.last_node = node
        self._float_down(self.root)
        print()
        print_layers([my_heap.root])
        print()
        print(self.last_node.data)
        return value

    def _float_up(self, node: Node):
        if node is not self.root and node.priority < node.parent.priority:
            self._swap(node, node.parent)
            self._float_up(node.parent)

    def _float_down(self, node: Node):
        if node.left is not None and node.left.priority < node.priority:
            if (node.right is not None and
                    node.right.priority < node.left.priority):
                self._swap(node.right, node)
                self._float_down(node.right)
                return
            self._swap(node.left, node)
            self._float_down(node.left)
        elif node.right is not None and node.right.priority < node.priority:
            self._swap(node.right, node)
            self._float_down(node.right)

    def _swap(self, node_a, node_b):
        node_a.data, node_b.data = node_b.data, node_a.data
        node_a.priority, node_b.priority = node_b.priority, node_a.priority

    def inorder(self):
        for node in self.__inorder_subtree(self.root):
            yield node.data

    def __inorder_subtree(self, node):
        if node is not None:
            for l_node in self.__inorder_subtree(node.left):
                yield l_node
            yield node
            for r_node in self.__inorder_subtree(node.right):
                yield r_node

    def __iter__(self):
        return self.inorder()

    def __str__(self):
        return " ".join(map(str, self.inorder()))


def print_layers(nodes):
    next_layer = list()
    for node in nodes:
        if node is not None:
            print(node.data, end=" ")
            next_layer.append(node.left)
            next_layer.append(node.right)
        else:
            print(" ", end=" ")
    if next_layer:
        print()
        print_layers(next_layer)


my_heap = Heap()
for i in range(20, -1, -1):
    my_heap.add(i, i)
print(my_heap)
print_layers([my_heap.root])
while my_heap.root is not None:
    print(my_heap.remove())
