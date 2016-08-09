from random import random
from time import time

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    arr = [int(1000*random()) for _ in range(1000)]
    origin_arr = arr[:]

    s_time = time()
    bubble_sort(arr)
    if sorted(origin_arr) == arr:
        print("버블정렬 완료")
    else:
        print("버블정렬 안됨.")
    print((time()-s_time)*60)