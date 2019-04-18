class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def sum_of_items(head):
    if head is None:
        return 0
    return head.value + sum_of_items(head.next)


if __name__ == "__main__":

    print("TESTING SUM OF ITEMS - MAKE BETTER TESTS!!!\n")

    this_list = Node(1, Node(4, Node(2, Node(7, None))))
    print(sum_of_items(this_list))

    # my tests

    this_list = None
    print(sum_of_items(this_list))

    this_list = Node(0)
    print(sum_of_items(this_list))

    this_list = Node(0, Node(4, Node(6)))
    print(sum_of_items(this_list))

    this_list = Node(0.5, Node(4.12, Node(6.5)))
    print(sum_of_items(this_list))  # floating point precision...
