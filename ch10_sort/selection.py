from random import random
from time import time

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[max_idx] > arr[j]:
                max_idx = j

        arr[max_idx], arr[i] = arr[i], arr[max_idx]

if __name__ == '__main__':
    arr = [int(1000*random()) for _ in range(1000)]
    origin_arr = arr[:]

    s_time = time()
    selection_sort(arr)
    if sorted(origin_arr) == arr:
        print("선택정렬 완료")
    else:
        print("선택정렬 안됨.")
    print((time()-s_time)*60)

