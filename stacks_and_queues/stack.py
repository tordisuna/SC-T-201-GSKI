class Stack(object):
    def __init__(self, base_capacity=4):
        self.capacity = base_capacity
        self.size = 0
        self.arr = [0] * base_capacity

    def _resize(self):
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.size):
            new_array[i] = self.arr[i]
        self.arr = new_array

    def push(self, element):
        if self.size == self.capacity:
            self._resize()
        self.arr[self.size] = element
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.arr[self.size]

    def peek(self):
        return self.arr[self.size]
