def length(a_string):
    if not a_string:
        return 0
    return 1 + length(a_string[:-1])


print(length("Abc123"))