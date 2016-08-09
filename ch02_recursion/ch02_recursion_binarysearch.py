from timeit import default_timer as timer
import sys

from ch01_intro.ch01_search import binary_search


def binary_search2(arr, target, first, last, op_cnt):

    if first > last:
        return -1

    mid = first + last

    if arr[mid] == target:
        return arr[mid]
    elif arr[mid] > target:
        return binary_search2(arr, target, first, mid-1, op_cnt)
    else:
        return binary_search2(arr, target, mid+1, last, op_cnt)

sys.setrecursionlimit(20000)

array = [x for x in range(20000)]

start = timer()
print(binary_search2(array, 19999, 0, len(array)-1, 0))
print((timer() - start)*60, "\n")

start = timer()
print(binary_search(array, 19999))
print((timer() - start)*60, "\n")