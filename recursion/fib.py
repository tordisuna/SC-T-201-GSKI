def fib(n):
    '''Return n-th fibonacci number'''
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# print(fib(100))


def better_fib(n, a=1, b=1):
    if n <= 1:
        return a
    return better_fib(n-1, a + b, a)

for i in range(10):
    print(better_fib(i))