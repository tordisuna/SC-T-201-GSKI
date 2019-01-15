from random import randint


def random_number_insertion(size: int):
    '''
    Creates a list of specified size with random numbers between 1 and 6,
    Complexity: O(n)
    '''
    return [randint(1, 6) for _ in range(size)]
