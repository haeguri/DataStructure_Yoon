from random import random
from time import time

def interpolation_search(arr, first, last, target, method="bi"):
    if arr[first] > target or arr[last] < target:
        print("타겟이 없다.")
        return None

    if method == "bi":
        mid = (first+last)//2
    elif method == "ip":
        mid = int((target-arr[first])*(last-first)/(arr[last]-arr[first]) + first)
    else:
        print("인자를 똑바로 입력하세요")
        return None

    if arr[mid] == target:
        print("타겟 발견. 위치는 ", mid)
        return mid
    elif arr[mid] > target:
        last = mid - 1
        return interpolation_search(arr, first, last, target)
    else:
        first = mid + 1
        return interpolation_search(arr, first, last, target)

if __name__ == '__main__':
    arr = [int(random()*10000000) for _ in range(10000000)]
    arr.sort()

    s_time = time()
    print(interpolation_search(arr, 0, len(arr)-1, 33333))
    bi_time = (time()-s_time)
    print("이진검색 소요시간", bi_time)

    s_time = time()
    print(interpolation_search(arr, 0, len(arr)-1, 33333, "ip"))
    ip_time = (time()-s_time)
    print("보간검색 소요시간", ip_time)

    print("보간검색이 이진검색보다 %s배 빠릅니다." % (bi_time/ip_time))