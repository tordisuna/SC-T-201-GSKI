from dataclasses import dataclass, field


class Node(object):
    pass


@dataclass()
class Node(object):
    priority: object
    data: object = None
    parent: Node = None
    left_child: Node = None
    right_child: Node = None


class Heap(object):
    def __init__(self, *args, **kwargs):
        self.root = self.last_node = None

    def add(self, value, priority):
        if self.root is None:
            self.root = self.last_node = Node(priority, value)
            self.root.parent = Node(0, 0)
        elif self.last_node.parent.left_child is self.last_node and self.last_node is not self.root:
            new_node = Node(priority, value, self.last_node)
            self.last_node.parent.right_child = new_node
            self.last_node = new_node
        else:
            node = self.last_node
            while node.parent.right_child is node:
                node = node.parent
            if node is not self.root:
                node = node.parent.right_child
            while node.left_child is not None:
                node = node.left_child
            node.left_child = self.last_node = Node(priority, value, node)
        #self.float_node(self.last_node)

    def float_node(self, node: Node):
        if node is not self.root and node.data >= node.parent.data:
            node.data, node.parent.data = node.parent.data, node.data
            self.float_node(node.parent)


my_heap = Heap()
for i in range(20):
    my_heap.add(i, i)
print(my_heap)
