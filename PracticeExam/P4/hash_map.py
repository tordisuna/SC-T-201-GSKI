from bucket import *


class HashMap:
    def __init__(self, *args, **kwargs):
        self.buckets = [Bucket() for i in range(16)]
        self.size = 0

    def _get_bucket(self, key):
        return self.buckets[hash(key) % 16]

    def __getitem__(self, key):
        try:
            return self._get_bucket(key).find(key)
        except NotFoundException:
            return None

    def __setitem__(self, key, value):
        bucket = self._get_bucket(key)
        try:
            bucket.insert(key, value)
            self.size += 1
        except ItemExistsException:
            bucket.update(key, value)

    def __delitem__(self, key):
        try:
            self._get_bucket(key).remove(key)
            self.size -= 1
        except NotFoundException:
            pass

    def __len__(self):
        return self.size


if __name__ == "__main__":

    print("\nTESTING HASHMAP - MAKE BETTER TESTS!!")
    m = HashMap()
    m[3] = "Value for key: 3"
    m[6] = "Value for key: 6"
    m[2] = "Value for key: 2"

    print("")
    print(str(m[2]))
    print(str(m[3]))
    print(str(m[4]))
    print(str(m[5]))
    print(str(m[6]))
    print("Size of collection: " + str(len(m)))

    del m[3]

    print("")
    print(str(m[2]))
    print(str(m[3]))
    print(str(m[4]))
    print(str(m[5]))
    print(str(m[6]))
    print("Size of collection: " + str(len(m)))

    del m[4]

    print("")
    print(str(m[2]))
    print(str(m[3]))
    print(str(m[4]))
    print(str(m[5]))
    print(str(m[6]))
    print("Size of collection: " + str(len(m)))
