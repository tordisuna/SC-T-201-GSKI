class Node(object):
    def __init__(self, element=None, next=None):
        self.element = element
        self.next = next


class PriorityQueue(object):
    def __init__(self, *args, **kwargs):
        self.head = None

    def sorted_add_recur(self, new_node: Node, current: Node):
        if current.next is None:
            current.next = new_node
        elif new_node.element < current.next.element:
            new_node.next = current.next
            current.next = new_node
        else:
            self.sorted_add_recur(new_node, current.next)

    def add(self, element):
        new_node = Node(element)
        if self.head is not None and self.head.element <= new_node.element:
            self.sorted_add_recur(new_node, self.head)
        else:
            new_node.next = self.head
            self.head = new_node

    def remove(self):
        if self.head is not None:
            element = self.head.element
            self.head = self.head.next
            return element

if __name__ == "__main__":
    p = PriorityQueue()
    p.add(5)
    p.add(9)
    p.add(3)
    p.add(7)
    print(p.remove())
    print(p.remove())
    print(p.remove())
    print(p.remove())
    print(p.remove())
