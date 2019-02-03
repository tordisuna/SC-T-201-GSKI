class Deque(object):
    def __init__(self, base_capacity=4):
        self.capacity = base_capacity
        self.back = 0
        self.front = 0
        self.items = 0
        self.arr = [0] * base_capacity

    def _resize(self):
        if self.front != self.back:
            raise ValueError("WTF!?")
        old_cap = self.capacity
        self.capacity *= 2
        new_array = [0] * self.capacity
        jag = self.items - self.front
        for i in range(self.front, old_cap):
            new_array[i - self.front] = self.arr[i]
        for i in range(self.front):
            new_array[i + jag] = self.arr[i]
        self.front = 0
        self.back = self.items
        self.arr = new_array

    def push_back(self, value):
        if self.items == self.capacity:
            self._resize()
        self.arr[self.back] = value
        self.items += 1
        self.back = (self.front + self.items) % self.capacity

    def pop_front(self):
        if not self.items:
            return
        self.front += 1
        self.front %= self.capacity
        item = self.arr[self.front]
        self.items -= 1
        if not self.items:
            self.front = 0
            self.back = 0
        return item

    def push_front(self, value):
        if self.items == self.capacity:
            self._resize()
        self.arr[self.front] = value
        self.items += 1
        self.front = (self.front - 1) % self.capacity

    def pop_back(self):
        if not self.items:
            return
        item = self.arr[self.back]
        self.back -= 1
        self.back %= self.capacity
        self.items -= 1
        if not self.items:
            self.front = 0
            self.back = 0
        return item

    def get_size(self):
        return self.items
