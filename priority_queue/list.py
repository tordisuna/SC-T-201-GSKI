class PriorityQueue(object):
    def __init__(self, *args, **kwargs):
        self.list = list()

    def add(self, value, priority):
        for i, item in enumerate(self.list):
            if priority > item[1]:
                self.list.insert(i, (value, priority))
                return
        self.list.append((value, priority))

    def remove(self):
        if self.list:
            return self.list.pop()


if __name__ == "__main__":
    p = PriorityQueue()
    p.add("A", 5)
    p.add("C", 9)
    p.add("B", 3)
    p.add("D", 7)
    print(p.remove())
    print(p.remove())
    print(p.remove())
    print(p.remove())
    print(p.remove())
