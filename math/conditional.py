from random import choice
coin = ["H", "T"]
head_first = 0
head_first_and_four_heads = 0
for i in range(100000):
    flips = [choice(coin) for _ in range(5)]
    if flips[0] == "H":
        head_first_and_four_heads += flips.count("H") == 4
        head_first += 1

print(head_first_and_four_heads / head_first)
