# def multiply(a, b):
#     if b == 0:
#         return 0
#     if b == 1:
#         return a
#     return a + multiply(a, b - 1)


def multiply(a, b):
    if a < 0 and b < 0:
        return multiply(-a, -b)
    elif a < 0 or b < 0:
        return -multiply(abs(a), abs(b))
    elif b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + multiply(a, b - 1)

print(multiply(-5, 6))