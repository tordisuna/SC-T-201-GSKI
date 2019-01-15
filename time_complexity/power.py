def exponentiation(a, n):
    '''Raises a to the power b'''
    return a ** n


def loop_power(a, n):
    '''Raises a to the power b, O(n)'''
    for i in range(n):
        a *= a
    return a


def shift_power(a, n):
    '''Raises a to the power b, O(log n)'''
    result = 1
    while True:
        if n % 2 == 1:
            result = a * result
        n = n >> 1
        if n == 0:
            return result
        a = a * a

# Testing for accuracy
for n in range(1000):
    for k in range(1000):
        assert exponentiation(n, k) == shift_power(n, k)
