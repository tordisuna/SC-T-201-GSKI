def multiplication(n: int, k: int):
    '''Returns product of n and k, O(n)'''
    result = 0
    if n > k:
        n, k = k, n
    if n < 0:
        k = -k
        n = -n
    for i in range(n):
        result += k
    return result

# Testing for accuracy
for n in range(-1000, 1000):
    for k in range(-1000, 1000):
            product = multiplication(n, k)
            assert n * k == product
