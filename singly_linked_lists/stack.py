from node import Node 


class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_top = Node(value, self.top)
        self.top = new_top
        self.size += 1

    def pop(self):
        if self.top is not None:
            value = self.top.value
            self.top = self.top.next
            self.size -= 1
            return value

    def get_size(self):
        return self.size


my_stack = Stack()
for i in range(100):
    my_stack.push(i)

print("Size: ", my_stack.get_size())

for _ in range(101):
    print(my_stack.pop())
