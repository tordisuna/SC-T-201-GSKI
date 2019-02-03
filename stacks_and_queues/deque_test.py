from collections import deque
from random import randint
from deque import Deque



a = Deque()
b = deque()
for i in range(10000):
    rand_op = randint(0, 3)
    rand_value = randint(0, 10000)
    if rand_op == 0:
        # push_front
        a.push_front(rand_value)
        b.appendleft(rand_value)
    elif rand_op == 1:
        # push back
        a.push_back(rand_value)
        b.append(rand_value)
    elif rand_op == 2:
        # pop front
        try:
            b_pop = b.popleft()
        except IndexError:
            b_pop = None
        a_pop = a.pop_front()
        assert a_pop == b_pop
    elif rand_op == 3:
        try:
            b_pop = b.pop()
        except IndexError:
            b_pop = None
        a_pop = a.pop_back()        
        assert a_pop == b_pop
