class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LL(object):
    def __init__(self, *args, **kwargs):
        self.head = None
        self.tail = self.head

    def add(self, data):
        self.head = Node(data, self.head)

    def __str__(self):
        return " ".join(map(str, self.rev_items(self.head)))

    def items(self, node):
        if node is not None:
            yield node.data
            yield from self.items(node.next)

    def rev_items(self, node):
        if node is not None:
            yield from self.rev_items(node.next)
            yield node.data

    def range(self, lo, hi):
        for item in self.items(self.head):
            if lo <= item <= hi:
                yield item

    def get_range(self, lo, hi):
        return list(self.range(lo, hi))


if __name__ == "__main__":
    ll = LL()
    from random import randint
    for i in range(100):
        ll.add(randint(0, 10000))
    print(ll)
    print(*ll.range(0, 200))
