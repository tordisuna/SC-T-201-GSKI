
# Gudni Natan Gunnarsson
# SC-T-201-GSKI
# Hlutaprof 2, 2019


class DataClass:
    # USE THIS IMPLEMENTATION OF DATACLASS UNCHANGED
    def __init__(self, x_type, x_information):
        self.x_type = x_type
        self.x_information = x_information

    def __str__(self):
        return "{" + str(self.x_type) + ": " + str(self.x_information) + "}"


class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

# Part 1


def count_value(head, value):
    if head is None:
        return 0
    if head.data == value:
        return 1 + count_value(head.next, value)
    return count_value(head.next, value)


def contains(head, value):  # slightly more efficient than using count_value
    if head is None:
        return False
    if head.data == value:
        return True
    return contains(head.next, value)


def contains_all(head1, head2):
    if head2 is None:
        return True
    if not contains(head1, head2.data):
        return False
    return contains_all(head1, head2.next)

# Part 2


class DLL_Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DataList:
    def __init__(self):
        self.__header = DLL_Node()
        self.__trailer = DLL_Node(None, self.__header)
        self.__header.next = self.__trailer

    def add_to_front(self, value):
        node = DLL_Node(value, self.__header, self.__header.next)
        self.__header.next.prev = node
        self.__header.next = node

    def add_to_back(self, value):
        node = DLL_Node(value, self.__trailer.prev, self.__trailer)
        self.__trailer.prev.next = node
        self.__trailer.prev = node

    def __str__(self):
        ret_str = ""
        node = self.__header
        while node is not self.__trailer.prev:
            node = node.next
            ret_str += str(node.value) + " "
        node = node.next
        if node is not self.__trailer:
            ret_str += str(node.value)
        return ret_str

    # Part 3

    def delete_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def get_all_of_type(self, type, remove_from_original=False):
        dl = DataList()
        node = self.__header.next
        while node is not self.__trailer:
            if node.value.x_type == type:
                dl.add_to_back(node.value)
                if remove_from_original:
                    self.delete_node(node)
            node = node.next
        return dl


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("DataClass example:")
    dc = DataClass(2, "A string with some information for type 2")
    print(str(dc))
    dc = DataClass(3, "A string with information for type 3 DataClass")
    print(str(dc))
    dc = DataClass(2, "More information for a type 2 D.C.")
    print(str(dc))

    print("Singly-linked node example:")
    head = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5)))))
    print(str(head))

    print("\nTesting count_value")
    head = SLL_Node(1, SLL_Node(2, SLL_Node(1, SLL_Node(1, SLL_Node(5)))))
    print("list:  ", head)
    print("# of 1:", count_value(head, 1))
    print("# of 4:", count_value(head, 4))
    print("# of 5:", count_value(head, 5))
    head = None
    print(count_value(head, 6))
    head = SLL_Node()
    print(count_value(head, 4))
    print(count_value(head, None))

    print("\nTesting contains_all")
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(
        3, SLL_Node(4, SLL_Node(5, SLL_Node(6, SLL_Node(7)))))))
    head2 = SLL_Node(5, SLL_Node(2, SLL_Node(1)))
    head3 = SLL_Node(5, SLL_Node(2, SLL_Node(0)))
    head4 = SLL_Node(6, SLL_Node(1, SLL_Node(3)))
    head5 = None
    print("{" + str(head1) + "} contains all in {" +
          str(head2) + "}:", contains_all(head1, head2))
    print("{" + str(head1) + "} contains all in {" +
          str(head3) + "}:", contains_all(head1, head3))
    print("{" + str(head1) + "} contains all in {" +
          str(head4) + "}:", contains_all(head1, head4))
    print("{" + str(head1) + "} contains all in {" +
          str(head5) + "}:", contains_all(head1, head5))
    print("{" + str(head5) + "} contains all in {" +
          str(head1) + "}:", contains_all(head5, head1))
    print("{" + str(head1) + "} contains all in {" +
          str(head1) + "}:", contains_all(head1, head1))
    print("{" + str(head3) + "} contains all in {" +
          str(head1) + "}:", contains_all(head3, head1))
    print("{" + str(head2) + "} contains all in {" +
          str(head1) + "}:", contains_all(head2, head1))

    print("\nTesting DataList")
    d1 = DataList()
    d1.add_to_back(1)
    d1.add_to_back(2)
    d1.add_to_back(3)
    print("dl:", d1)
    d1 = DataList()
    d1.add_to_front(3)
    d1.add_to_front(2)
    d1.add_to_front(1)
    print("dl:", d1)
    d1 = DataList()
    d1.add_to_front(2)
    d1.add_to_back(3)
    d1.add_to_front(1)
    print("dl:", d1)

    print("\nTesting get_all_of_type")
    dl1 = DataList()
    dl1.add_to_back(DataClass(1, "I: type 1"))
    dl1.add_to_back(DataClass(2, "O: type 2"))
    dl1.add_to_back(DataClass(3, "type 3 DataClass"))
    dl1.add_to_back(DataClass(1, "Other type 1"))
    dl1.add_to_back(DataClass(2, "More info: type 2"))
    dl1.add_to_back(DataClass(1, "Type 1 D.C."))
    print("dl1:", dl1)
    dl2 = dl1.get_all_of_type(2)
    print("dl2:", dl2)
    print("dl1:", dl1)
    dlasd = dl1.get_all_of_type("asd")
    print("dlasd:", dlasd)
    print("dl1:", dl1)
    dl3 = dl1.get_all_of_type(1, True)
    print("dl3:", dl3)
    print("dl1:", dl1)
    dl2 = dl1.get_all_of_type(2, True)
    dl4 = dl1.get_all_of_type(3, True)
    print("dl2:", dl2)
    print("dl4:", dl4)
    print("dl1:", dl1)
    dl5 = dl1.get_all_of_type(6, True)
    print("dl5:", dl5)
