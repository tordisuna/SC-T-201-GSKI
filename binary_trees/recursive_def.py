from math import inf


class EBT(object):
    def __init__(self, node: int, left_subtree=None, right_subtree=None):
        self.node = node
        self.lt = left_subtree
        self.rt = right_subtree

    def largest(self) -> int:
        node = self.node
        left = self.lt.largest() if self.lt else -inf
        right = self.rt.largest() if self.rt else -inf
        if node >= left and node >= right:
            return node
        elif left >= node and left >= right:
            return left
        else:
            return right

    def least(self) -> int:
        node = self.node
        left = self.lt.least() if self.lt else inf
        right = self.rt.least() if self.rt else inf
        if node <= left and node <= right:
            return node
        elif left <= node and left <= right:
            return left
        else:
            return right

    def is_bst(self) -> bool:
        if self.lt:
            if self.lt.node <= self.node or not self.lt.is_bst():
                return False
        if self.rt and not self.rt.is_bst():
            if self.rt.node >= self.node or not self.rt.is_bst():
                return False
        return True


# def largest(tree: EBT) -> int:
#     if tree.lt is None and tree.rt is None:
#         return tree.node
#     elif tree.lt is None and tree.node >= largest(tree.rt):
#         return tree.node
#     elif tree.lt is None and tree.node < largest(tree.rt):
#         return largest(tree.rt)
#     elif tree.rt is None and tree.node >= largest(tree.lt):
#         return tree.node
#     elif tree.rt is None and tree.node < largest(tree.lt):
#         return largest(tree.lt)
#     elif tree.node >= largest(tree.lt) and tree.node >= largest(tree.rt):
#         return tree.node
#     elif largest(tree.lt) >= largest(tree.rt) and largest(tree.lt) >= tree.node:
#         return largest(tree.lt)
#     else:
#         return largest(tree.rt)


def largest(tree: EBT):
    if tree.lt is None:
        if tree.rt is None:
            return largest_node(tree)
        return largest_right(tree)
    elif tree.rt is None:
        return largest_left(tree)
    else:
        return largest_full(tree)


def largest_node(tree: EBT):
    return tree.node


def largest_full(tree: EBT):
    left = largest(tree.lt)
    right = largest(tree.rt)
    node = tree.node
    if node >= left and node >= right:
        return node
    elif left >= node and left >= right:
        return left
    else:
        return right


def largest_right(tree: EBT):
    right = largest(tree.rt)
    node = tree.node
    if node > right:
        return node
    return right


def largest_left(tree: EBT):
    left = largest(tree.lt)
    node = tree.node
    if node > left:
        return node
    return left


def pythonic_largest(tree: EBT):
    node = tree.node
    left = pythonic_largest(tree.lt) if tree.lt else -inf
    right = pythonic_largest(tree.rt) if tree.rt else -inf
    if node >= left and node >= right:
        return node
    elif left >= node and left >= right:
        return left
    else:
        return right


def least(tree: EBT):
    node = tree.node
    left = least(tree.lt) if tree.lt else inf
    right = least(tree.rt) if tree.rt else inf
    if node <= left and node <= right:
        return node
    elif left <= node and left <= right:
        return left
    else:
        return right


a1 = EBT(4)
a2 = EBT(1, a1)
a3 = EBT(5)
a4 = EBT(2, a2, a3)
a5 = EBT(4, None, a4)

print(largest(a5))
print(a5.least())
print(a5.is_bst())