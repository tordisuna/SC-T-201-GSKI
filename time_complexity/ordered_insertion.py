from random import randint
import timeit
from insertion import random_number_insertion


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
    while low < high:
        mid = (low + high) // 2
        if a_list[mid] < number:
            low = mid + 1
        else:
            high = mid
    return low


def linear_insert(a_list: list, number: int):
    '''Single insert in O(n) time'''
    index = linear_search(a_list, number)
    insert(a_list, number, index)


def binary_insert(a_list: list, number: int):
    '''Single insert using binary search, still in O(n) time because
    of the insert.'''
    index = binary_search(a_list, number)
    insert(a_list, number, index)


def test_insert(insert_function, a_list):
    '''Populates sorted list, complexity: O(n^2)'''
    my_list = list()
    for num in a_list:
        insert_function(my_list, num)
    return my_list

if __name__ == "__main__":
    testlist = random_number_insertion(1000)

    start_time = timeit.default_timer()
    sorted_list_1 = test_insert(linear_insert, testlist)
    print(timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    sorted_list_2 = test_insert(binary_insert, testlist)
    print(timeit.default_timer() - start_time)

    for i, item in enumerate(zip(sorted_list_1, sorted_list_2)):
        if item[0] != item[1]:
            print(i)

    assert sorted_list_1 == sorted_list_2
