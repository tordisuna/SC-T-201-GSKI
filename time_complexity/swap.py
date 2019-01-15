from random import randint
from insertion import random_number_insertion
from random_increase import random_index


def random_index_tuple(a_list: list) -> tuple:
    '''Picks two seperate random indices of a list and returns a tuple, O(1).
    Raises ValueError if the list contains fewer than 2 elements.'''
    index1 = random_index(a_list)
    index2 = randint(0, len(a_list) - 2)
    if index2 >= index1:
        index2 += 1
    assert index1 != index2
    return (index1, index2)


def swap(a_list, indices):
    index1, index2 = indices
    a_list[index1], a_list[index2] = a_list[index2], a_list[index1]


def switch_random(a_list: list):
    '''Switches two random neighbor elements in a list, O(1)'''
    index = random_index(a_list)
    swap(a_list, (index, index - 1))


def swap_random(a_list: list):
    '''Swaps two random elements in a list, O(1)'''
    indices = random_index_tuple(a_list)
    swap(a_list, indices)


def generate_and_swap(n: int):
    '''Generates a list of size n and swaps two elements in the list, O(n)'''
    my_list = random_number_insertion(n)
    swap_random(my_list)

if __name__ == "__main__":
    my_list = random_number_insertion(10)
    print(my_list)
    swap(my_list)
    print(my_list)
