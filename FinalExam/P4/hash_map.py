class NotFoundException(Exception):
    pass


class ValuePair(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        if type(other) == type(self):
            return self.key == other.key
        return self.key == other


class HashMap:
    BUCKET_COUNT = 16

    def __init__(self):
        self.buckets = [list() for i in range(self.BUCKET_COUNT)]
        self.size = 0

    def __setitem__(self, key, data):
        item = ValuePair(key, data)
        bucket = self.buckets[key % self.BUCKET_COUNT]
        try:
            index = bucket.index(item)
            bucket[index] = item
        except ValueError:
            bucket.append(item)
            self.size += 1

    def __getitem__(self, key):
        bucket = self.buckets[key % self.BUCKET_COUNT]
        try:
            index = bucket.index(key)
            return bucket[index].value
        except ValueError:
            raise NotFoundException()

    def __len__(self):
        return self.size


if __name__ == "__main__":

    print("\nTESTING HASHMAP - MAKE BETTER TESTS!!")

    m = HashMap()
    m[3] = "Value for key: 3"
    m[6] = "Value for key: 6"
    m[2] = "Value for key: 2"

    print("")
    try:
        print(str(m[2]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[3]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[4]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[5]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[6]))
    except(NotFoundException):
        print("Item not found")
    print("Size of collection: " + str(len(m)))
