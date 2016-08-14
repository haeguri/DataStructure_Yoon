from ch07_queue.list_base_queue import ListBaseQueue
from random import random

def radix_sort(arr):
    max_n = 0

    for n in arr:
        if max_n < n:
            max_n = n

    max_len = len(str(max_n))

    bucket_list = [ListBaseQueue() for _ in range(10)]

    fac = 1

    for _ in range(max_len):
        for n in arr:
            radix = n // fac % 10
            bucket_list[radix].enqueue(n)

        i = 0

        for bucket in bucket_list:
            while not bucket.is_empty():
                arr[i] = bucket.dequeue()
                i += 1

        fac *= 10

if __name__ == '__main__':
    origin_arr = [int(100*random()) for _ in range(100)]
    radix_sort(origin_arr)

    print(origin_arr)