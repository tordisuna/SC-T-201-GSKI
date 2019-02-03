import timeit
from insertion import random_number_insertion
from ordered_insertion import binary_insert, linear_insert
from swap import swap


def sorted_list(a_list):
    '''Creates a sorted list in O(n^2) time'''
    new_list = list()
    for item in a_list:  # n times
        linear_insert(new_list, item)  # O(n)
    return new_list


def sort(a_list):
    '''Insertion sort in place, O(n^2) time'''
    for i in range(1, len(a_list)):
        element = a_list[i]
        for j in range(i - 1, -1, -1):
            sorted_element = a_list[j]
            if element < sorted_element:
                swap(a_list, (j, j + 1))
            else:
                break

if __name__ == "__main__":
    my_list = random_number_insertion(30)
    print(my_list)
    print(sorted_list(my_list))
    sort(my_list)
    print(my_list)

my_list = [i for i in range(1000)]
my_list.reverse()
# print(my_list)
start_time = timeit.default_timer()
a_list = sort(my_list)
print(timeit.default_timer() - start_time)
#print(my_list)