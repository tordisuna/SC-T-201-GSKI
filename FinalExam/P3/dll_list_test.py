from random import choice, randrange
from dll_list import DLL


def test_insert(dll, pylist, pos, value):
    dll.insert(value)
    pylist.insert(pos, value)
    return pos


def test_remove(dll, pylist, pos, value):
    dll.remove()
    try:
        pylist.pop(pos)
    except IndexError:
        assert dll.curr.data is None
    return pos


def test_move_to_next(dll, pylist, pos, value):
    dll.move_to_next()
    return min(pos + 1, len(pylist))


def test_move_to_prev(dll, pylist, pos, value):
    dll.move_to_prev()
    return max(pos - 1, 0)


def test_len(dll, pylist, pos, value):
    assert len(dll) == len(pylist)
    return pos


def test_str(dll, pylist, pos, value):
    pylist_str = ""
    for item in pylist:
        pylist_str += str(item) + " "
    dll_str = str(dll)
    assert dll_str == pylist_str
    return pos


if __name__ == "__main__":
    test_functions = [test_insert, test_remove,
                      test_move_to_next, test_move_to_prev, test_len, test_str]
    for i in range(1000):
        my_ll = DLL()
        my_list = list()
        pos = 0
        for i in range(10000):
            val = randrange(0, 10000)
            fun = choice(test_functions)
            pos = fun(my_ll, my_list, pos, val)
