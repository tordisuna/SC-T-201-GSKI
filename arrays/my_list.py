class ArrayList(object):
    def __init__(self, base_capacity=4):
        self.capacity = base_capacity
        self.size = 0
        self.arr = [0] * base_capacity

    def append(self, element):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = element
        self.size += 1

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

    def shrink(self):
        if self.size * 4 <= self.capacity:
            self.capacity //= 2
            new_array = [0] * self.capacity
            for i in range(self.size):
                new_array[i] = self.arr[i]
            self.arr = new_array

    def insert(self, index, element):
        if index > self.size:
            index = self.size
        if self.size == self.capacity:
            self.shift_resize(index)
        else:
            for i in range(self.size, index, -1):
                self.arr[i] = self.arr[i-1]
        self.arr[index] = element
        self.size += 1

    def pop(self, index=-1):
        if index < 0:
            index += self.size
        if index > self.size:
            raise IndexError("pop index out of range")
        item = self.arr[index]
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        self.size -= 1
        self.shrink()
        return item

    def prepend(self, element):
        self.insert(0, element)

    def __len__(self):
        return self.size

    def get_at(self, index):
        return self.arr[index]

    def get_first(self):
        return self.arr[0]

    def print_array_list(self):
        print(self)

    def sort(self):
        '''Insertion sort in place, O(n^2) time'''
        for i in range(1, self.size):
            element = self.arr[i]
            for j in range(i - 1, -1, -1):
                sorted_element = self.arr[j]
                if element < sorted_element:
                    self[j], self[j + 1] = self[j + 1], self[j]
                else:
                    break

    def __str__(self):
        string = str()
        for i in range(self.size - 1):
            string += str(self.arr[i]) + ", "
        if self.size > 0:
            string += str(self.arr[self.size - 1])
        return string

    def __getitem__(self, key):
        if key < 0:
            key += self.size
        if key < self.size:
            return self.arr[key]
        raise IndexError()

    def __setitem__(self, key, value):
        self.arr[key] = value

    def __delitem__(self, key):
        self.pop(key)

a = ArrayList()
for i in range(20):
    a.append(i + 1)

print(a)

a.sort()

print(a)

print(max(a))

for i in range(len(a)):
    a.pop()

print(a)
