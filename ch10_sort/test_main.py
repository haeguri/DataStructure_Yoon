from random import random
from time import time
from ch10_sort.bubble import bubble_sort
from ch10_sort.selection import selection_sort
from ch10_sort.insertion import insertion_sort
from ch10_sort.merge import merge_sort
from ch10_sort.quick import quick_sort

if __name__ == '__main__':
    origin_arr = [int(10000*random()) for _ in range(10000)]

    merge_arr = origin_arr[:]
    bubble_arr = origin_arr[:]
    selection_arr = origin_arr[:]
    insertion_arr = origin_arr[:]
    quick_arr = origin_arr[:]

    s_time = time()
    merge_sort(merge_arr, 0, len(merge_arr)-1)
    if merge_arr == sorted(origin_arr):
        print("_________________________________")
        print("병합정렬 소요시간 :", (time()-s_time))
        print("병합 정렬 완료.")
        print("_________________________________")
    else:
        print("병합 정렬 실패")

    s_time = time()
    bubble_sort(bubble_arr)
    if bubble_arr == sorted(origin_arr):
        print("_________________________________")
        print("버블정렬 소요시간 :", (time()-s_time))
        print("버블정렬 완료.")
        print("_________________________________")
    else:
        print("버블 정렬 실패")

    s_time = time()
    selection_sort(selection_arr)
    if selection_arr == sorted(origin_arr):
        print("_________________________________")
        print("선택정렬 소요시간 :", (time()-s_time))
        print("선택정렬 완료.")
        print("_________________________________")
    else:
        print("선택정렬 실패")

    s_time = time()
    insertion_sort(insertion_arr)
    if insertion_arr == sorted(origin_arr):
        print("_________________________________")
        print("삽입정렬 소요시간 :", (time()-s_time))
        print("삽입정렬 완료.")
        print("_________________________________")
    else:
        print("삽입정렬 실패")

    s_time = time()
    quick_sort(quick_arr, 0, len(quick_arr)-1)
    if quick_arr == sorted(origin_arr):
        print("_________________________________")
        print("퀵정렬 소요시간 :", (time()-s_time))
        print("퀵정렬 완료.")
        print("_________________________________")
    else:
        print("퀵정렬 실패")