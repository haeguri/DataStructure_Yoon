from random import random
from time import time

def merge_sort(arr, left, right):
    if left < right:
        mid = (left+right)//2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)

        merge_to_area(arr, left, mid, right)

def merge_to_area(arr, left, mid, right):
    f_idx = left
    r_idx = mid + 1

    s_idx = left
    s_arr = [0 for _ in range(right+1)]

    while f_idx <= mid and r_idx <= right:
        if arr[f_idx] <= arr[r_idx]:
            s_arr[s_idx] = arr[f_idx]
            s_idx += 1
            f_idx += 1
        else:
            s_arr[s_idx] = arr[r_idx]
            s_idx += 1
            r_idx += 1

    if f_idx > mid:
        for i in range(r_idx, right+1):
            s_arr[s_idx] = arr[i]
            s_idx += 1
    else:
        for i in range(f_idx, mid+1):
            s_arr[s_idx] = arr[i]
            s_idx += 1

    print("sort_arr", s_arr)

    for i in range(left, right+1):
        arr[i] = s_arr[i]

    del s_arr

from ch10_sort.bubble import bubble_sort
from ch10_sort.selection import selection_sort
from ch10_sort.insertion import insertion_sort

if __name__ == '__main__':

    origin_arr = [int(10*random()) for _ in range(10)]

    merge_arr = origin_arr[:]


    s_time = time()
    merge_sort(merge_arr, 0, len(merge_arr)-1)
    if merge_arr == sorted(origin_arr):
        print("_________________________________")
        print("병합정렬 소요시간 :", (time()-s_time)*60)
        print("병합 정렬 완료.")
        print("_________________________________")
    else:
        print("병합 정렬 실패")