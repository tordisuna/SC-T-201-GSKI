from random import randint
from hashlib import sha1
from math import inf
import timeit


def string_hash(a_string):
    my_hash = 1239
    for c in a_string:
        my_hash = my_hash * 127 + ord(c)
    return my_hash % 2147483647


def num_hash(an_int):
    my_hash = an_int
    for _ in range(100):
        my_hash = my_hash * 127 + an_int
        my_hash %= 2147483647
    return my_hash


def cycle(an_int: int, digits: int):
    digits %= 32
    mask = (1 << 32) - 1
    return (an_int << digits & mask) | an_int >> (digits - 32)


def random_string(min_len=5, max_len=20):
    string = ""
    for _ in range(randint(min_len, max_len)):
        string += chr(randint(65, 80))
    return string


def get_ratio(a_list):
    if min(a_list) == 0:
        return inf
    diff = max(a_list) - min(a_list)
    return diff / min(a_list)


def test_num_hash(item_count, bucket_count, common_factor=1):
    numbers = [randint(0, 10000) * common_factor for _ in range(item_count)]

    list_len = bucket_count
    my_list = [0] * list_len
    sha_list = [0] * list_len
    py_hash_list = [0] * list_len

    start_time = timeit.default_timer()
    for num in numbers:
        my_list[num_hash(num) % list_len] += 1
    print(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    hashId = sha1()
    for num in numbers:
        hashId.update(repr(num).encode('utf-8'))
        hashed_num = int.from_bytes(hashId.digest(), byteorder='big')
        sha_list[hashed_num % list_len] += 1
    print(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    for num in numbers:
        py_hash_list[hash(num) % list_len] += 1
    print(timeit.default_timer() - start_time)

    print("My ratio:", get_ratio(my_list))
    print("Sha1 ratio:", get_ratio(sha_list))
    print("hash() ratio:", get_ratio(py_hash_list))


def test_str_hash(item_count, bucket_count):
    strings = [random_string() for _ in range(item_count)]
    list_len = bucket_count
    my_list = [0] * list_len
    sha_list = [0] * list_len
    py_hash_list = [0] * list_len

    start_time = timeit.default_timer()
    for string in strings:
        my_list[string_hash(string) % list_len] += 1
    print(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    hashId = sha1()
    for string in strings:
        hashId.update(string.encode('utf-8'))
        hashed_num = int.from_bytes(hashId.digest(), byteorder='big')
        sha_list[hashed_num % list_len] += 1
    print(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    for string in strings:
        py_hash_list[hash(string) % list_len] += 1
    print(timeit.default_timer() - start_time)

    print("My ratio:", get_ratio(my_list))
    print("Sha1 ratio:", get_ratio(sha_list))
    print("hash() ratio:", get_ratio(py_hash_list))


if __name__ == "__main__":
    test_str_hash(10000, 12)
    # test_num_hash(10000, 100, 8)
