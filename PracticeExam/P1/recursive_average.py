
class SLL_Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

# IMPLEMENT THIS


def average_of_list(head):
    if head is None:
        return None
    total, length = average_recur(head)
    return total / length


def average_recur(head, length=0):
    if head.next is None:
        return head.data, length + 1
    total, length = average_recur(head.next, length)
    return head.data + total, length + 1


if __name__ == "__main__":
    # MAKE BETTER TESTS!
    print(average_of_list(SLL_Node(7, SLL_Node(5, SLL_Node(7, SLL_Node(5, None))))))
    print(average_of_list(SLL_Node(1, SLL_Node(3, SLL_Node(2, SLL_Node(4, None))))))
    print(average_of_list(SLL_Node(7, SLL_Node(5, SLL_Node(6, None)))))
    print(average_of_list(None))
