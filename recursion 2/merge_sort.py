from random import shuffle
import timeit


def merge_sort(m: list):
    # Base case. A list of zero or one elements is sorted, by definition.
    if len(m) <= 1:
        return m

    # Recursive case. First, divide the list into equal-sized sublists
    # consisting of the first half and second half of the list.
    # This assumes lists start at index 0.
    left = list()
    right = list()
    for i in range(len(m) // 2):
        left.append(m[i])
    for i in range(len(m) // 2, len(m)):
        right.append(m[i])

    # Recursively sort both sublists.
    left = merge_sort(m[:len(m) // 2])
    right = merge_sort(m[len(m) // 2:])

    # Then merge the now-sorted sublists.
    return merge(left, right)


def merge_sort(m, lo=0, hi=None):
    if hi is None:
        hi = len(m)
    if hi - lo == 1:
        return [m[lo]]
    if hi - lo == 0:
        return []
    mid = (hi + lo) // 2
    left = merge_sort(m, lo, mid)
    right = merge_sort(m, mid, hi)
    return merge(left, right)


def merge(left, right):
    left_start = 0
    right_start = 0
    result = list()
    while len(left) > left_start and len(right) > right_start:
        if left[left_start] <= right[right_start]:
            result.append(left[left_start])
            left_start += 1
        else:
            result.append(right[right_start])
            right_start += 1
    for i in range(left_start, len(left)):
        result.append(left[i])
    for i in range(right_start, len(right)):
        result.append(right[i])
    return result


# def merge(result, left, right, left_end=0, right_end=0):
#     if len(left) > left_end and len(right) > right_end:
#         if left[left_end] <= right[right_end]:
#             result.append(left[left_end])
#             return merge(result, left, right, left_end + 1, right_end)
#         result.append(right[right_end])
#         return merge(result, left, right, left_end, right_end + 1)
#     elif len(left) > left_end:
#         result.append(left[left_end])
#         return merge(result, left, right, left_end + 1, right_end)
#     elif len(right) > right_end:
#         result.append(right[right_end])
#         return merge(result, left, right, left_end, right_end + 1)
#     return result


# def merge(left: list, right: list):
#     result = list()
#     left.reverse()
#     right.reverse()

#     while left and right:
#         if left[-1] <= right[-1]:
#             result.append(left.pop())
#         else:
#             result.append(right.pop())

#     # Either left or right may have elements left; consume them.
#     # (Only one of the following loops will actually be entered.)
#     result.extend(reversed(left))
#     result.extend(reversed(right))
#     return result


my_list = [i for i in range(1000000)]
my_list.reverse()
# shuffle(my_list)
# print(my_list)
start_time = timeit.default_timer()
my_list = merge_sort(my_list)
print(timeit.default_timer() - start_time)
# print(my_list)