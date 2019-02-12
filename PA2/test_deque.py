import random
from collections import deque
from deque import ArrayDeque

if __name__ == "__main__":
    dq = ArrayDeque()
    dq.arr = [1, 2, None, 0]
    dq.front = 2
    dq.back = 3
    dq.size = 3
    print(dq)
    dq._resize(1)
    print(dq)

    a = deque()
    b = ArrayDeque()
    assert a.append("A") == b.append("A")
    assert " ".join(str(i) for i in a) == str(b)
    assert a.pop() == b.pop()
    assert " ".join(str(i) for i in a) == str(b)
    for i in range(50):
        if random.randint(0, 1):
            assert a.append(i) == b.append(i)
        else:
            assert a.appendleft(i) == b.appendleft(i)
    print(" ".join(str(i) for i in a))
    print(b)
    assert " ".join(str(i) for i in a) == str(b)
    for i in range(25):
        if random.randint(0, 1):
            assert a.pop() == b.pop()
        else:
            assert a.popleft() == b.popleft()

    assert " ".join(str(i) for i in a) == str(b)
    for i in range(50):
        if random.randint(0, 1):
            assert a.append(i) == b.append(i)
        else:
            assert a.appendleft(i) == b.appendleft(i)
    assert " ".join(str(i) for i in a) == str(b)
    for i in range(75):
        if random.randint(0, 1):
            assert a.pop() == b.pop()
        else:
            assert a.popleft() == b.popleft()
    assert " ".join(str(i) for i in a) == str(b)
