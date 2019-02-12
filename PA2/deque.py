class ArrayDeque(object):
    def __init__(self):
        self.capacity = 4
        self.front = self.back = 0
        self.arr = [None] * self.capacity
        self.size = 0

    def push_back(self, value):
        if self.capacity == self.size:
            self._resize(1)
        # Update location of back before array
        self.back = (self.back - 1) % self.capacity
        self.arr[self.back] = value
        self.size += 1

    def push_front(self, value):
        if self.capacity == self.size:
            self._resize(0)
        # Update array before location of front
        self.arr[self.front] = value
        self.front = (self.front + 1) % self.capacity
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            return None
        element = self.arr[self.back]
        self.back = (self.back + 1) % self.capacity
        self.size -= 1
        return element

    def pop_front(self):
        if self.is_empty():
            return None
        self.front = (self.front - 1) % self.capacity
        self.size -= 1
        return self.arr[self.front]

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size <= 0

    def __str__(self):
        string = ""
        if self.is_empty():
            return string
        if self.front > self.back:
            for i in range(self.back, self.front - 1):
                string += str(self.arr[i]) + " "
        else:
            for i in range(self.back, self.capacity):
                string += str(self.arr[i]) + " "
            for i in range(self.front - 1):
                string += str(self.arr[i]) + " "
        return string + str(self.arr[self.front - 1])

    def _resize(self, offset=0):
        '''Resize with optional offset. Doubles the size of the underlying
        array. Offset should not be more than self.size - 1. Additionally it
        rearranges the elements so they do not wrap circularly.
        '''
        new_arr = [None] * (self.capacity * 2)
        if self.front > self.back:
            for i in range(self.back, self.front):
                new_arr[i - self.back + offset] = self.arr[i]
        if self.front <= self.back:
            for i in range(self.back, self.capacity):
                new_arr[i - self.back + offset] = self.arr[i]
            # new_arr should now have self.capacity - self.back elements
            new_offset = self.capacity - self.back + offset
            # Reorder all the elements from 0 to self.front in the new array
            for i in range(self.front):
                new_arr[i + new_offset] = self.arr[i]
        # Update trackers
        self.capacity *= 2
        self.arr = new_arr
        self.back = offset
        self.front = self.size + offset

    # Equivalent collections.deque functions
    def append(self, element):
        return self.push_front(element)

    def appendleft(self, element):
        return self.push_back(element)

    def pop(self):
        return self.pop_front()

    def popleft(self):
        return self.pop_back()
