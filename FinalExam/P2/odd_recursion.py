def print_odd(value):
    odd_rec(value, 1)
    print()


def odd_rec(value, n=1):
    if n > value:
        return
    print(n, end=" ")
    odd_rec(value, n + 2)


if __name__ == "__main__":

    print("TESTING PRINT_ODD - MAKE BETTER TESTS!!!\n")

    print_odd(16)
    print_odd(15)
    print_odd(17)

    # my tests
    print_odd(-4)
    print_odd(0)
    print_odd(1)
