def bin_search(a_list, item):
    mid = len(a_list) // 2
    if a_list[mid] == item:
        return mid
    if len(a_list) == 1:
        raise ValueError(str(item) + " not found")
    if a_list[mid] < item:
        return mid + bin_search(a_list[mid:], item)
    return bin_search(a_list[:mid], item)


def bin_search(a_list, item, lo, hi):
    mid = (hi + lo) // 2
    if a_list[mid] == item:
        return mid
    if (hi - lo) == 1:
        raise ValueError(str(item) + " not found")
    if a_list[mid] < item:
        return bin_search(a_list, item, mid, hi)
    return bin_search(a_list, item, lo, mid)

my_list = [i for i in range(30)]
try:
    print(bin_search(my_list, 0, 0, 30))
except ValueError as e:
    print(e)
