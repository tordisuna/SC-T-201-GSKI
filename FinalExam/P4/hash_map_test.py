from random import randrange, choice
from hash_map import HashMap, NotFoundException


def test_setitem(hashmap, my_dict, key, value):
    hashmap[key] = value
    my_dict[key] = value


def test_getitem(hashmap, my_dict, key, value):
    try:
        assert hashmap[key] == my_dict[key]
    except NotFoundException:
        assert key not in my_dict


def test_len(hashmap, my_dict, key, value):
    assert len(hashmap) == len(my_dict)


if __name__ == "__main__":
    test_functions = [test_setitem, test_getitem, test_len]
    for i in range(1000):
        my_map = HashMap()
        my_dict = dict()
        for i in range(10000):
            key = randrange(0, 1000)
            val = randrange(0, 10000)
            choice(test_functions)(my_map, my_dict, key, val)
