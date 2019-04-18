from random import randrange, choice
from array_set import ArraySet


def test_add(my_set: ArraySet, pyset: set, value: int):
    my_set.add(value)
    pyset.add(value)


def test_len(my_set: ArraySet, pyset: set, value: int):
    assert len(my_set) == len(pyset)


def test_contains(my_set: ArraySet, pyset: set, value: int):
    a = value in pyset
    b = value in my_set
    assert a == b


def test_str(my_set: ArraySet, pyset: set, value: int):
    my_str = str(my_set)
    py_str = " ".join([str(item) for item in sorted(pyset)]) + " "
    assert my_str == py_str or (my_str == '' and py_str == " ")


if __name__ == "__main__":
    test_functions = [test_add, test_len, test_contains, test_str]
    for i in range(1000):
        bst = ArraySet()
        pyset = set()
        for i in range(1000):
            val = randrange(0, 1000)
            choice(test_functions)(bst, pyset, val)
