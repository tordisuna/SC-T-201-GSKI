from random import shuffle
a = [1, 2, 3, 4]

total = 0
for _ in range(10000):
    shuffle(a)
    total += a.index(4) < a.index(2) and a.index(4) < a.index(1)
print(total / 10000)
