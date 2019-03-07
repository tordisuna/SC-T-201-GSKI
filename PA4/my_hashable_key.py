class MyHashableKey(object):
    MASK = (1 << 32) - 1

    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self, other):
        return (self.int_value == other.int_value and
                self.string_value == other.string_value)

    def __hash__(self):
        my_hash = self.int_value
        for c in self.string_value:
            my_hash = self.cycle(my_hash, ord(c))
            my_hash = my_hash * 127 + self.int_value
            my_hash %= 2147483647
        return my_hash

    def cycle(self, an_int: int, digits: int):
        digits %= 32
        return (an_int << digits & self.MASK) | an_int >> (32 - digits)
