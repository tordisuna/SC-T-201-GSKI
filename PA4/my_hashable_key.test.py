from random import randint
from math import inf
from my_hashable_key import MyHashableKey
from hash_map import HashMap


def random_string(min_len=0, max_len=20):
    string = ""
    for _ in range(randint(min_len, max_len)):
        string += chr(randint(65, 80))
    return string


def bucket_sizes(a_map):
    for bucket in a_map.buckets:
        yield len(bucket)


def get_ratio(a_map):
    sizes = list(bucket_sizes(a_map))
    diff = max(sizes) - min(sizes)
    print(diff, max(sizes))
    return diff / max(sizes)


def main():
    keys = list()
    for _ in range(randint(1000, 100000)):
        keys.append(MyHashableKey(randint(0, 10000), random_string()))

    my_map = HashMap()
    for key in keys:
        if key not in my_map:
            my_map[key] = 0
        my_map[key] += 1

    return get_ratio(my_map)


total = 0
for i in range(1):
    total += main()

print(total / 10)
