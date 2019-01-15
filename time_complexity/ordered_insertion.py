from random import randint
import timeit


def insert(a_list: list, number: int, index: int):
    '''Inserts the number into the list at index, O(n)'''
    a_list.insert(index, number)


def linear_search(a_list: list, number: int):
    '''Gets you the index number should go to keep order, O(n)'''
    for i, list_num in enumerate(a_list):
        if list_num >= number:
            return i
    else:
        return len(a_list)


def binary_search(a_list: list, number: int):
    low = 0
    high = len(a_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if a_list[mid] < number:
            low = mid + 1
        elif a_list[mid] > number:
            high = mid - 1
        else:
            return mid
    return len(a_list)


def linear_insert(a_list: list, number: int):
    '''Single insert in O(n) time'''
    index = linear_search(a_list, number)
    insert(a_list, number, index)


def binary_insert(a_list: list, number: int):
    '''Single insert using binary search, still in O(n) time because
    of the insert.'''
    index = binary_search(a_list, number)
    insert(a_list, number, index)


def test_insert(n, insert_function):
    '''Populates sorted list, complexity: O(n^2)'''
    my_list = list()
    for _ in range(n):
        insert_function(my_list, randint(1, 6))

if __name__ == "__main__":
    start_time = timeit.default_timer()
    test_insert(100000, linear_insert)
    print(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    test_insert(100000, binary_insert)
    print(timeit.default_timer() - start_time)