from set import MySet


class Array(object):
    def __init__(self, ):
        self.array = [None] * 4
        self.size = 0

    def add(self, data):
        if self.size == len(self.array):
            self.resize()
        self.array[self.size] = data
        self.size += 1

    def resize(self):
        old_array = self.array
        self.array = [None] * len(self.array) * 2
        for i, data in enumerate(old_array):
            self.array[i] = data

    def __str__(self):
        string = ""
        for i in range(self.size):
            string += str(self.array[i]) + " "
        return string

    def __contains__(self, data):
        return data in self.array

    def remove_duplicates(self):
        count = 0
        other = MySet()
        for i in range(self.size):
            data = self.array[i]
            if data in other:
                count += 1
            else:
                self.array[i - count] = self.array[i]
                other.add(data)
        self.size -= count


if __name__ == "__main__":
    array = Array()
    from random import randint
    for i in range(1000):
        array.add(randint(0, 10))
    print(array)
    array.remove_duplicates()
    print(array)
