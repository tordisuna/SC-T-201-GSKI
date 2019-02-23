from itertools import product


def implies(a, b):
    '''a implies b boolean'''
    return bool(not a or b)


def do_logic(r, p, q):
    print(r, p, q, ": ", implies((r and p), (r and q)))


def do_logic2(r, p, q):
    print(r, p, q, ": ", implies(p, q) or not r)

for r, p, q in product(range(2), repeat=3):
    do_logic(r, p, q)

print()
for r, p, q in product(range(2), repeat=3):
    do_logic2(r, p, q)
