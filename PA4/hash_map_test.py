from random import randint, choice
from hash_map import HashMap
from bucket import ItemExistsException, NotFoundException

my_dict = dict()
my_hash_map = HashMap()


def check_insert(key, value):
    if key in my_dict:
        try:
            my_hash_map.insert(key, value)  # This should throw an exception
            assert 0 == 1
        except ItemExistsException:
            pass
    else:
        my_dict[key] = value
        my_hash_map.insert(key, value)
        assert len(my_dict) == len(my_hash_map)
        assert my_dict[key] == my_hash_map[key]
    assert (0.59 < (len(my_hash_map) - 1) / my_hash_map.bucket_count <= 1.2 or
            len(my_hash_map) < 5)


def check_find(key, value):
    try:
        assert my_dict[key] == my_hash_map.find(key)
    except KeyError:
        assert key not in my_hash_map


def check_contains(key, value):
    in_dict = key in my_dict
    in_map = my_hash_map.contains(key)
    assert in_dict == in_map


def check_update(key, value):
    try:
        my_hash_map.update(key, value)
        my_dict[key] = value
        assert my_dict[key] == my_hash_map[key]
    except NotFoundException:
        assert key not in my_dict


def check_remove(key, value):
    try:
        my_hash_map.remove(key)
        my_dict.pop(key)
        assert not my_hash_map.contains(key)
        assert len(my_hash_map) == len(my_dict)
    except NotFoundException:
        assert key not in my_dict


def check_len(key, value):
    assert len(my_dict) == len(my_hash_map)


checking_functions = [check_insert, check_find, check_contains,
                      check_update, check_len]

if __name__ == "__main__":
    for _ in range(100000):
        key = randint(-100, 100)
        value = randint(-100, 100)
        choice(checking_functions)(key, value)
