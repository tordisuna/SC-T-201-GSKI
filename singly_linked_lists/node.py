from random import randint


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
    if head is None:
        return Node(data)
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


def length(head: Node) -> int:
    if head is None:
        return 0
    return 1 + length(head.next)


def length_iterative(head: Node) -> int:
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def ll_sum(head: Node) -> int:
    if head is None:
        return 0
    return head.value + ll_sum(head.next)


def ll_ordered_insert(head, value):
    if head is None or head.value > value:
        return Node(value, head)
    cur_node = head
    while cur_node.next is not None:
        if cur_node.next.value > value:
            cur_node.next = Node(value, cur_node.next)
            return head
        cur_node = cur_node.next
    cur_node.next = Node(value)
    return head


def ll_ord_insrt_recursive(head, value):
    if head is None or head.value > value:
        return Node(value, head)
    head.next = ll_ord_insrt_recursive(head.next, value)
    return head


def reverse_ll(head):
    if head is None or head.next is None:
        return head
    next_node = head.next
    back = reverse_ll(next_node)
    next_node.next = head
    head.next = None
    return back


def double_reverse_ll(head, last=None):
    '''Reverses a linked list and then reverses it again restoring original
    behavior
    '''
    if head is None:
        return True
    next_node = head.next
    head.next = last
    if next_node is None:
        if last is None:
            return True
        return head
    bottom = double_reverse_ll(next_node, head)
    if last is not None:
        last.next = head
    else:
        penultimate = bottom.next
        penultimate.next = bottom.next = None
        pal = double_reverse_ll(head.next)
        penultimate.next = bottom
        return pal and head.value == bottom.value
    return bottom


def merge_lists(head_1, head_2):
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    if head_1.value <= head_2.value:
        head_1.next = merge_lists(head_1.next, head_2)
        return head_1
    head_2.next = merge_lists(head_1, head_2.next)
    return head_2


def split_list(head):
    half_node = head
    end_node = head
    while end_node.next is not None and end_node.next.next is not None:
        end_node = end_node.next.next
        half_node = half_node.next
    other_head = half_node.next
    half_node.next = None
    return head, other_head


def merge_sort(head):
    if head is None or head.next is None:
        return head
    headlen = length(head)
    node_a, node_b = split_list(head)
    assert length(node_a) + length(node_b) == headlen
    node_a = merge_sort(node_a)
    node_b = merge_sort(node_b)
    merged = merge_lists(node_a, node_b)
    assert length(merged) == headlen
    return merged


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
    print(length(d))
    print(length_iterative(d))

    a = None
    for i in range(20):
        a = push_back(a, i)
    print(ll_sum(a))
    b = None
    for _ in range(3):
        b = ll_ordered_insert(b, randint(1, 100))

    print()
    print_ll(b)

    c = None
    for _ in range(2):
        c = ll_ord_insrt_recursive(c, randint(1, 100))
    print()

    print_ll_recursive(c)

    print()
    d = merge_lists(b, c)
    print_ll(d)
    print("end of merge list")
    print()
    e = None
    for _ in range(5):
        e = push_front(e, randint(1, 100))

    print_ll(e)
    print()
    e = merge_sort(e)
    print_ll(e)

    test = Node('A', Node('B', Node('C', None)))
    look = test.next
    pal = double_reverse_ll(test)
    print_ll_recursive(test)
    print(pal)
    test2 = Node('A', Node('B', Node('B', Node('A', None))))
    print(double_reverse_ll(test2))
    print_ll_recursive(test2)
