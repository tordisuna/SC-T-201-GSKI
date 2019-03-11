from random import randint
# import your version of MyHashableKey here:
from my_hashable_key import MyHashableKey


def random_string(min_len=1, max_len=20):
    '''Creates and returns a random string of english upper-case characters'''
    string = ""
    for _ in range(randint(min_len, max_len)):
        string += chr(randint(65, 90))
    return string


def get_ratio(buckets):
    diff = max(buckets) - min(buckets)
    # print("Size:", len(buckets), "Diff:", diff, ", max:", max(buckets))
    return (diff / max(buckets))


def test_with_bucket_list(bucket_count: int, items_per_bucket=100,
                          common_factor=4):
    '''Use this to test your MyHashableKey implementation, and get
    distribution'''
    keys = list()
    for _ in range(items_per_bucket * bucket_count):
        random_number = randint(0, 100000) * common_factor
        keys.append(MyHashableKey(random_number, random_string()))
    buckets = [0] * bucket_count
    for key in keys:
        buckets[hash(key) % bucket_count] += 1
    return get_ratio(buckets)


def test_random_distribution(bucket_count: int, items_per_bucket=100):
    '''Use this to compare to a completely random distribution'''
    buckets = [0] * bucket_count
    for _ in range(items_per_bucket * bucket_count):
        buckets[randint(0, bucket_count - 1)] += 1
    return get_ratio(buckets)


def test_python_hash_distribution(bucket_count, items_per_bucket=100):
    '''Use this to compare to pythons default implementation of hashing'''
    buckets = [0] * bucket_count
    for _ in range(items_per_bucket * bucket_count):
        result = randint(0, 100000) ^ hash(random_string())
        buckets[result % bucket_count] += 1
    return get_ratio(buckets)

# RATIO INFORMATION
# Lower score = better
# 0 = perfect (all buckets have equally many items)
# 1 = super bad (at least one of the buckets has no items)
#
# Average distribution ratio of 0.35 is very good!
# That means your distribution is pretty much random.
# My high score is 0.345


for i in range(100):
    if __name__ == "__main__":
        total = 0
        test_count = 100
        for i in range(4, test_count + 4):
            ratio = test_with_bucket_list(bucket_count=i)
            total += ratio
            # print(ratio)

        print("Average distribution ratio:", total / test_count)
