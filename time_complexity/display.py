from insertion import random_number_insertion


def print_to_screen(element, a_list):
    '''
    Prints element and list to screen, O(n) time with n being the size of
    the list. It goes through the list two times, but since constants are
    removed the time is still O(n)
    '''
    print(element)
    stringified_list = [str(i) for i in a_list]   # Time complexity: O(n)
    print(", ".join(stringified_list))   # Time complexity: O(n)


def display(a_list):
    '''displays list info, O(n^2)'''
    for element in a_list:
        print_to_screen(element, a_list)  # O(n)

display(random_number_insertion(5))
