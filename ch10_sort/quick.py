from random import random

def partition(arr, left, right):
    pivot = arr[left]
    low = left + 1
    high = right

    while low <= high:
        while low <= right and pivot >= arr[low] :
            low += 1

        while high >= left+1 and pivot <= arr[high]:
            high -= 1

        if low <= high:
            arr[high], arr[low] = arr[low], arr[high]

    arr[high], arr[left] = arr[left], arr[high]
    return high

def quick_sort(arr, left, right):
    if left <= right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot-1)
        quick_sort(arr, pivot+1, right)

if __name__ == '__main__':
    arr = [int(10*random()) for _ in range(10)]

    origin_arr = arr[:]

    quick_sort(arr, 0, len(arr)-1)

    print(arr)



