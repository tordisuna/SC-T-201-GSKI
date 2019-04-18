
class ArraySet:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = [None] * self.capacity

    def add(self, value):
        # using the sorted insert route
        index = self._binary_search(value)
        if index == self.size or self.arr[index] != value:
            if self.size == self.capacity:
                self._resize()
            for i in range(self.size, index, - 1):
                self.arr[i] = self.arr[i - 1]
            self.arr[index] = value
            self.size += 1

    def _resize(self):
        old_arr = self.arr
        self.capacity *= 2
        self.arr = [None] * self.capacity
        for i in range(self.size):
            self.arr[i] = old_arr[i]

    def __contains__(self, value):
        index = self._binary_search(value)
        return index != self.size and self.arr[index] == value

    def _linear_search(self, val):
        for i in range(self.size):
            if self.arr[i] >= val:
                return i
        return self.size

    def _binary_search(self, val):
        """Find the index where val is, or where to insert it."""
        if self.size == 0:
            return 0
        return self._bisect_recursive(val, 0, self.size)

    def _bisect_recursive(self, val, lo, hi):
        mid = (lo + hi) // 2
        if self.arr[mid] == val:
            return mid
        if lo == mid:
            return lo if self.arr[mid] > val else hi
        elif self.arr[mid] > val:
            return self._bisect_recursive(val, lo, mid)
        elif self.arr[mid] < val:
            return self._bisect_recursive(val, mid, hi)

    def __str__(self):
        my_str = ""
        for i in range(self.size):
            my_str += str(self.arr[i]) + " "
        return my_str

    def __len__(self):
        return self.size


if __name__ == "__main__":

    print("\nTESTING ARRAY SET - MAKE BETTER TESTS!!\n")

    lis = ArraySet()
    lis.add(4)
    print(lis)

    lis.add(2)
    print(lis)

    lis.add(7)
    print(lis)

    lis.add(1)
    print(lis)

    lis.add(11)
    print(lis)

    lis.add(2)
    print(lis)

    lis.add(9)
    print(lis)

    # extra testing
    lis.add(9)
    print(lis)

    lis.add(12)
    print(lis)

    lis.add(9)
    print(lis)

    print(lis.size)
    print(lis.capacity)
    lis.add(3)
    lis.add(8)

    print(lis.capacity)
    from random import randint
    for i in range(1000):
        lis.add(randint(0, 99))
    print(lis)
    print(lis.size)
    print(lis.capacity)

    lis = ArraySet()
    lis.add(4)
    lis.add(4)
    print(lis)
    for i in range(1000):
        lis.add(randint(0, 99))
    print(lis)
    print(lis.size)
    print(lis.capacity)
    print(1 in lis)

    print(all((i in lis for i in range(100))))
    lis.add(1.1)
    print(lis.arr)
