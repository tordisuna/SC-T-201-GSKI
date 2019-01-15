from random import randint
from insertion import random_number_insertion


def random_index(a_list):
    return randint(0, len(a_list) - 1)


def random_increase(a_list):
    '''Increases a random number in a list, O(1)'''
    index = random_index(a_list)  # Assuming randint and len runs in O(1)
    a_list[index] += 1  # O(1)

if __name__ == "__main__": 
    # Tests for accuracy
    for _ in range(200):
        my_list = random_number_insertion(10)
        prelim_sum = sum(my_list)
        random_increase(my_list)
        assert sum(my_list) == prelim_sum + 1

    my_list = random_number_insertion(10)
    prelim_sum = sum(my_list)
    for _ in range(200):
        random_increase(my_list)
        assert sum(my_list) == prelim_sum + 1
        prelim_sum += 1
