from random import randint
from math import inf
from my_hashable_key import MyHashableKey


def random_string(min_len=0, max_len=20):
    string = ""
    for _ in range(randint(min_len, max_len)):
        string += chr(randint(65, 80))
    return string


def get_ratio(a_list):
    if min(a_list) == 0:
        return inf
    diff = max(a_list) - min(a_list)
    return diff / min(a_list)


def main():
    keys = list()
    for _ in range(randint(1000, 100000)):
        keys.append(MyHashableKey(randint(0, 10000), random_string()))

    bucket_count = 40
    buckets = [0] * bucket_count
    for key in keys:
        buckets[hash(key) % bucket_count] += 1

    return get_ratio(buckets)

total = 0
for i in range(100):
    total += main()

print(total / 100)
