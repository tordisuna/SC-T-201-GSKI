from random import choice
biased = ("H", "H", "H", "T")
fair = ("H", "T")

total = 0
hits = 0
for i in range(1000000):
    coin = choice((biased, fair))
    result = ""
    for i in range(5):
        result += choice(coin)
    if result == "HHTHH":
        hits += coin == biased
        total += 1

print(hits / total)
