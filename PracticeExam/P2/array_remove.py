
class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def _resize(self):
        self.capacity *= 2
        tmp_arr = [None] * self.capacity
        for i in range(self.size):
            tmp_arr[i] = self.arr[i]
        self.arr = tmp_arr

    def append(self, value):
        if self.size == self.capacity:
            self._resize()
        self.arr[self.size] = value
        self.size += 1

    # IMPLEMENT THIS
    def remove(self, index):
        self.size -= 1
        for i in range(index, self.size):
            self.arr[i] = self.arr[i + 1]

    def __str__(self):
        ret_str = ""
        for i in range(self.size - 1):
            ret_str += str(self.arr[i]) + " - "
        return ret_str + str(self.arr[self.size - 1])


if __name__ == "__main__":
    lis = ArrayList()
    lis.append(1)
    lis.append(2)
    lis.append(3)
    lis.append(4)
    lis.append(5)
    lis.append(6)
    lis.append(7)
    lis.append(8)
    lis.append(9)
    lis.append(10)
    lis.append(11)

    print(lis)

    lis.remove(3)

    print(lis)
