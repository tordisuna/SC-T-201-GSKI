from random import randrange, choice, shuffle
from bst_set import BSTSet


def test_add(bst: BSTSet, pyset: set, value: int):
    bst.add(value)
    pyset.add(value)


def test_remove(bst: BSTSet, pyset: set, value: int):
    bst.remove(value)
    try:
        pyset.remove(value)
    except KeyError:
        pass


def test_len(bst: BSTSet, pyset: set, value: int):
    assert len(bst) == len(pyset)


def test_contains(bst: BSTSet, pyset: set, value: int):
    a = value in pyset
    b = bst.contains(value)
    assert a == b


if __name__ == "__main__":
    test_functions = [test_add, test_remove, test_len, test_contains]
    for i in range(200):
        bst = BSTSet()
        pyset = set()
        for i in range(1000):
            val = randrange(0, 500)
            choice(test_functions)(bst, pyset, val)

        items = list(range(500))
        shuffle(items)
        for i in items:
            test_remove(bst, pyset, i)

        test_len(bst, pyset, 0)

        shuffle(items)
        for i in items:
            test_remove(bst, pyset, i)

        for i in range(1000):
            val = randrange(0, 500)
            choice(test_functions)(bst, pyset, val)
