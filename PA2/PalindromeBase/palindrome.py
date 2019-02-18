class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def print_to_screen(head):
    if head is not None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

# Older version that uses a wrapper function and non-local
# I think it looks pretty, but the nonlocal is awkward
#
# def palindrome(head) -> bool:
#     def inner(inner_head) -> bool:
#         nonlocal head
#         if inner_head is None:
#             return True
#         value = inner(inner_head.next) and inner_head.data == head.data
#         head = head.next
#         return value
#     return inner(head)

# Strategy is to close in on both sides of the lists during the recursion exit
# Both sides meet in the middle, and then it's easy to determine whether it is
# A palindrome.
# No wrapper function is needed, but an extra parameter to keep track of the
# true head is necessary.
# Only needs to run down the list once and then up


def palindrome(head, top=None):
    '''Takes a head node and returns whether or not the linked list is a
    palindrome
    '''
    if top is None:  # if outermost call
        if head is None or head.next is None:
            return True  # returns True if length < 2
        top = head
    if head.next is None:
        return top, True  # head is bottom
    new_top, result = palindrome(head.next, top)
    if head is top:  # if outermost call
        return (head.next.data == new_top.data) and result
    result &= head.next.data == new_top.data
    return new_top.next, result


if __name__ == "__main__":

    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A")
    print(palindrome(head))

    head = Node(
        "A", Node("D", Node("B", Node("R", Node("B", Node("D", Node("A")))))))
    print(palindrome(head))
