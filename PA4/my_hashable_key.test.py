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
    print("Size:", len(buckets), "Diff:", diff, ", max:", max(buckets))
    return (diff / max(buckets))


def test_with_bucket_list(bucket_count: int, items_per_bucket=100,
                          common_factor=4):
    keys = list()
    for _ in range(items_per_bucket * bucket_count):
        random_number = randint(0, 10000) * common_factor
        keys.append(MyHashableKey(random_number, random_string()))
    buckets = [0] * bucket_count
    for key in keys:
        buckets[hash(key) % bucket_count] += 1
    return get_ratio(buckets)


def test_random_distribution(bucket_count: int, items_per_bucket=100):
    buckets = [0] * bucket_count
    for _ in range(items_per_bucket * bucket_count):
        buckets[randint(0, bucket_count - 1)] += 1
    return get_ratio(buckets)


if __name__ == "__main__":
    total = 0
    test_count = 100
    for i in range(4, test_count + 4):
        ratio = test_with_bucket_list(bucket_count=i)
        total += ratio
        print(ratio)

    print("Average ratio:", total / test_count)
