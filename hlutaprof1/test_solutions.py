import solutions
from solutions import *
from random import randint, randrange, random

assert sum_of_odd(3, 8) == 15

for _ in range(1000):
    rand_a = randint(-100, 500)
    rand_b = randint(-100, 500)
    rand_a, rand_b = min(rand_a, rand_b), max(rand_a, rand_b)
    odd_sum = sum_of_odd(rand_a, rand_b)
    loop_sum = 0
    for i in range(rand_a, rand_b + 1):
        if i % 2 == 1:
            loop_sum += i
    assert odd_sum == loop_sum


lis = [3, 6, -1]
raise_by_one(lis)
assert lis == [4, 7, 0]

for _ in range(100):
    comp = [randint(-1000, 1000) + random() for _ in range(500)]
    comp2 = comp[::1]
    raise_by_one(comp)

    for i in range(len(comp2)):
        assert comp2[i] + 1 == comp[i]


arr_list = ArrayList()
arr_list.prepend("str1")
arr_list.prepend("str2")
arr_list.print_list()
arr_list.set_at(1, "str3")
arr_list.print_list()

for i in range(1000):
    arr_list.prepend(i)
arr_list.print_list()
assert arr_list.get_size() == 1002


rental = Rental()
rental.add_car("MFT67", "chrysler", 5)
car = rental.get_car("MFT67")
car.set_brand("fiat")
print(rental)

rental.add_car("ABC", "WowzerBus", 40)
rental.add_car("12345", "my car", 100)
rental.add_car("23456", "your car", 200)
rental.add_car("34567", "our car", 103)
print(rental)
