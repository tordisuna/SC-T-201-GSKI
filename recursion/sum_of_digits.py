def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


def super_sum_of_digits(n):
    total = sum_of_digits(n)
    if total < 10:
        return total
    return super_sum_of_digits(total)
