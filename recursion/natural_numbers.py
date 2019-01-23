def natural_numbers(n):
    if n == 1:
        print(n, end=' ')
        return
    natural_numbers(n - 1)
    print(n, end=" ")

natural_numbers(5)