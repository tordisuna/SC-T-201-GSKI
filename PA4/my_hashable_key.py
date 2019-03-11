from random import randint


class MyHashableKey(object):
    MASK = (1 << 64) - 1
    M = 0xc6a4a7935bd1e995
    R = 47
    seed = randint(0, MASK)  # Random seed chosen on launch

    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self, other):
        return (self.int_value == other.int_value and
                self.string_value == other.string_value)

    def __hash__(self):
        '''Hash based on murmurhash'''
        my_hash = self.seed ^ self.int_value
        for c in self.string_value:
            number = (ord(c) * self.M) & self.MASK
            number ^= number >> self.R
            number = (number * self.M) & self.MASK
            my_hash = (my_hash * self.M) ^ (number * self.M)
            my_hash &= self.MASK
        my_hash ^= my_hash >> 13
        my_hash = (my_hash * self.M) & self.MASK
        my_hash ^= my_hash >> 15
        return my_hash
