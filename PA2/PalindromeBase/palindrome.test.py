from random import randint
from palindrome import palindrome, Node


def nodify(string) -> Node:
    head = None
    for c in reversed(string):
        head = Node(c, head)
    return head


def random_string(min_len=8, max_len=20):
    string = ""
    for _ in range(randint(min_len, max_len)):
        string += chr(randint(65, 80))
    return string


def generate_palindrome():
    string = random_string()
    return string + string[::-1]


def is_pal(string) -> bool:
    for i in range(len(string) // 2):
        if string[i] != string[-i-1]:
            return False
    return True


if __name__ == "__main__":
    for i in range(100):
        pal = generate_palindrome()
        pal_head = nodify(pal)
        assert palindrome(pal_head)

    for i in range(1000000):
        string = random_string()
        string_head = nodify(string)
        pal = is_pal(string)
        if pal:
            print(string)
        assert palindrome(string_head) == pal
