from dataclasses import dataclass


@dataclass(order=True, eq=True, frozen=True)
class MyComparableKey(object):
    integer_value: int
    string_value: str


if __name__ == "__main__":
    my_key = MyComparableKey(1, "asd")
    my_key2 = MyComparableKey(2, "a")
    my_key3 = MyComparableKey(2, "dfsdf")
    my_key4 = MyComparableKey(1, "asd")

    print(my_key < my_key2)
    print(my_key2 < my_key3)
    print(hash(my_key))
    print(hash(my_key4))
