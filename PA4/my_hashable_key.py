class MyHashableKey(object):
    MASK = (1 << 32) - 1

    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self, other):
        return (self.int_value == other.int_value and
                self.string_value == other.string_value)

    # def __hash__(self):
    #     my_hash = self.int_value
    #     for c in self.string_value:
    #         my_hash = (my_hash * 54059) ^ (ord(c) * 76963)
    #         my_hash = self.cycle(my_hash, self.int_value)

    #     return my_hash % 2147483647

    def __hash__(self):
        # mask = 0xffffffffffffffff
        my_hash = self.int_value
        if self.string_value:
            my_hash ^= (ord(self.string_value[0]) << 7)
        for c in self.string_value:
            my_hash = ((my_hash * 1000003) ^ ord(c)) % 2147483647
        return my_hash

    def cycle(self, an_int: int, digits: int):
        digits %= 32
        return (an_int << digits & self.MASK) | an_int >> (32 - digits)