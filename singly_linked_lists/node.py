class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def push_front(head, value):
    return Node(value, head)


def print_ll(node: Node):
    while node is not None:
        print(node.value)
        node = node.next


def print_ll_recursive(node: Node):
    if node is None:
        return
    print(node.value)
    print_ll_recursive(node.next)


def pop_front(head: Node):
    if head is not None:
        return head.next


def push_back(head: Node, data):
    node = head
    while node.next is not None:
        node = node.next
    node.next = Node(data)
    return head


def pop_back(head: Node):
    if head is None or head.next is None:
        return None
    current_node = head.next
    last_node = head
    while current_node.next is not None:
        last_node = current_node
        current_node = current_node.next
    last_node.next = None
    return head


if __name__ == "__main__":
    # Tests
    a = Node("a")
    b = push_front(a, "b")
    c = push_front(b, "c")

    print_ll(c)
    print_ll_recursive(c)

    d = pop_front(c)
    pop_back(d)
    d = push_back(d, "wow")

    print_ll(d)
