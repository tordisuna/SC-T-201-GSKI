from bucket import Bucket


class HashMap(object):
    def __init__(self, *args, **kwargs):
        self.bucket_count = 4
        self.buckets = [Bucket() for _ in range(self.bucket_count)]
        self.size = 0

    def insert(self, key, value):
        if len(self) >= self.bucket_count * 1.2:
            self.rebuild()
        index = self.get_hash(key)
        self.buckets[index].insert(key, value)
        self.size += 1

    def update(self, key, data):
        index = self.get_hash(key)
        self.buckets[index].update(key, data)

    def find(self, key):
        return self[key]

    def contains(self, key):
        index = self.get_hash(key)
        return key in self.buckets[index]

    def remove(self, key):
        index = self.get_hash(key)
        self.buckets[index].remove(key)
        self.size -= 1

    def __setitem__(self, key, data):
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.buckets[index][key]

    def __len__(self):
        return self.size

    def get_hash(self, key):
        return hash(key) % len(self.buckets)

    def rebuild(self):
        old_buckets = self.buckets
        self.bucket_count *= 2
        self.buckets = [Bucket() for _ in range(self.bucket_count)]
        self.size = 0
        for bucket in old_buckets:
            for item in bucket:
                self.insert(item.key, item.value)

    # For testing purposes
    def __str__(self):
        string = "{"
        for bucket in self.buckets:
            for item in bucket:
                string += f"{item.key}: {item.value}, "
        return string + "}"

    def __contains__(self, key):
        return self.contains(key)
