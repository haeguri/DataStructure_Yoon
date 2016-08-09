from random import random
from time import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        cmp_elem = arr[i]
        in_idx = i

        for j in range(i-1, -1, -1):
            if arr[j] > cmp_elem:
                arr[j+1] = arr[j]
            else:
                break

            in_idx = j


        arr[in_idx] = cmp_elem


if __name__ == '__main__':
    # arr = [int(5*random()) for _ in range(5)]
    arr = [1,0,4,3,4]
    origin_arr = arr[:]

    s_time = time()
    insertion_sort(arr)
    if sorted(origin_arr) == arr:
        print("삽입정렬 완료")
    else:
        print("삽입정렬 안됨.")
    print((time()-s_time)*60)





