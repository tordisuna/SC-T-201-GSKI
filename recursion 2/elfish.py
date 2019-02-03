def x_ish(a_string, x):
    if not x:
        return True
    if len(x) == 1:
        if not a_string:
            return False
        if a_string[-1] == x:
            return True
        return x_ish(a_string[:-1], x)
    if x_ish(a_string, x[-1]):
        return x_ish(a_string, x[:-1])
    return False


def x_ish(a_string, x):
    for char in x:
        for compare_char in a_string:
            if char == compare_char:
                break
        else:
            return False
    return True

print(x_ish("gagnaskipan", "iganpsk"))
print(x_ish("gagnaskipan", "gnAsk"))


