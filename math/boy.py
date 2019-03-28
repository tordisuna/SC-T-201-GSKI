from random import uniform

total = 0
iterations = 100000
for _ in range(iterations):
    boys = 0
    for _ in range(5):
        boys += uniform(0, 1) <= 0.51
    total += bool(boys)
print(total / iterations)
