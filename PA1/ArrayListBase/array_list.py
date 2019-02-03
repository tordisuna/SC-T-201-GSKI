class IndexOutOfBounds(Exception):
    pass


class NotFound(Exception):
    pass


class Empty(Exception):
    pass


class ArrayList:
    def __init__(self, base_capacity=4):
        self.capacity = base_capacity
        self.size = 0
        self.arr = [0] * base_capacity
        self.ordered = True

    # Time complexity: O(n) - linear time in size of list
    def print(self):
        print(self)

    # Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value, 0)

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index > self.size:
            return
        if self.size == self.capacity:
            self.shift_resize(index)
        else:
            for i in range(self.size, index, -1):
                self.arr[i] = self.arr[i-1]
        self.arr[index] = value
        self.size += 1
        self.ordered = False

    # Time complexity: O(1) - constant time
    def append(self, value):
        self.insert(value, self.size)

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        try:
            self[index] = value
        except IndexError:
            pass

    # Time complexity: O(1) - constant time
    def get_first(self):
        if not self.size:
            raise Empty()
        return self.get_at(0)

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        if 0 <= index < self.size:
            return self.arr[index]
        raise IndexOutOfBounds()

    # Time complexity: O(1) - constant time
    def get_last(self):
        if not self.size:
            raise Empty()
        return self.get_at(self.size - 1)

    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.shift_resize(self.size)

    def shift_resize(self, index):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(index):
            new_array[i] = self.arr[i]
        for i in range(index, self.size):
            new_array[i + 1] = self.arr[i]
        self.arr = new_array

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if index < 0 or index >= self.size:
            return
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        self.size -= 1

    # Time complexity: O(1) - constant time
    def clear(self):
        self.__init__()

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def insert_ordered(self, value):
        if not self.ordered:
            self.sort()
        index = self.binary_search(self.arr, value, 0, self.size)
        self.insert(value, index)
        self.ordered = True

    # Time complexity: O(n^2) - quadratic time in size of list
    # Time complexity: O(n log n) - linear * logarythmic time in size of list
    def sort(self):
        sorted_arary = self._merge_sort(0, self.size)
        for i in range(self.size):
            self.arr[i] = sorted_arary[i]
        self.ordered = True

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def find(self, value):
        if not self.ordered:
            return self.linear_search(self.arr, value)
        index = self.binary_search(self.arr, value, 0, self.size)
        if 0 <= index < self.size and self.arr[index] == value:
            return index
        raise NotFound()

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarythmic time in size of list
    def remove_value(self, value):
        try:
            index = self.find(value)
        except NotFound:
            return
        self.remove_at(index)

    def __str__(self):
        string = str()
        for i in range(self.size - 1):
            string += str(self.arr[i]) + ", "
        if self.size > 0:
            string += str(self.arr[self.size - 1])
        return string

    def __getitem__(self, key):
        return self.get_at(key)

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.arr[index] = value
        raise IndexError()

    def __delitem__(self, key):
        self.remove_at(key)

    def __len__(self):
        return self.size

    def binary_search(self, a_list, item, lo, hi):
        '''Returns the leftmost index to insert an item in the ordered
        list a_list so that order is maintained.
        '''
        mid = (hi + lo) // 2
        if hi - lo <= 1:
            if a_list[mid] < item and lo != hi:
                return mid + 1
            return mid
        elif a_list[mid] < item:
            return self.binary_search(a_list, item, mid, hi)
        return self.binary_search(a_list, item, lo, mid)

    def binary_search(self, a_list, item, lo, hi):
        mid = (hi + lo) // 2
        if hi - lo <= 1:
            if a_list[mid] < item and lo != hi:
                return mid + 1
            return mid
        elif a_list[mid] == item:
            return mid
        elif a_list[mid] < item:
            return self.binary_search(a_list, item, mid, hi)
        return self.binary_search(a_list, item, lo, mid)

    def linear_search(self, a_list, item, index=0):
        if index == self.size:
            raise NotFound()
        if a_list[index] == item:
            return index
        return self.linear_search(a_list, item, index + 1)

    def _merge_sort(self, lo, hi):
        if hi - lo == 1:
            my_list = ArrayList()
            my_list.append(self.arr[lo])
            return my_list
        elif hi - lo == 0:
            return ArrayList()
        mid = (hi + lo) // 2
        # Recursively sort both sublists.
        left = self._merge_sort(lo, mid)
        right = self._merge_sort(mid, hi)
        return self._merge(left, right)

    def _merge(self, left, right):
        left_start = 0
        right_start = 0
        result = ArrayList()
        while left.size > left_start and right.size > right_start:
            if left[left_start] <= right[right_start]:
                result.append(left[left_start])
                left_start += 1
            else:
                result.append(right[right_start])
                right_start += 1
        for i in range(left_start, left.size):
            result.append(left[i])
        for i in range(right_start, right.size):
            result.append(right[i])
        return result
