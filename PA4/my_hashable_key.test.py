from random import randint
from math import inf
from my_hashable_key import MyHashableKey


def random_string(min_len=0, max_len=20):
    string = ""
    for _ in range(randint(min_len, max_len)):
        string += chr(randint(65, 90))
    return string


def get_ratio(buckets):
    diff = max(buckets) - min(buckets)
    print("Diff:", diff, ", max:", max(buckets))
    print(buckets)
    return (diff / max(buckets))


def test_with_bucket_list(bucket_count: int, items_per_bucket=300):
    keys = list()
    for _ in range(items_per_bucket * bucket_count):
        keys.append(MyHashableKey(randint(0, 10000) * 4, random_string()))
    buckets = [0] * bucket_count
    for key in keys:
        buckets[hash(key) % bucket_count] += 1

    return get_ratio(buckets)

if __name__ == "__main__":
    total = 0
    for i in range(1, 101):
        ratio = test_with_bucket_list(bucket_count=i * 12)
        total += ratio
        print(ratio)

    print("Average ratio:", total / 100)
