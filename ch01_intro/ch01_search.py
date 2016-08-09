def sequencial_search(arr, target):
    op_cnt = 0
    for elem in arr:
        op_cnt += 1
        if elem == target:
            print("연산 횟수는 {0}".format(op_cnt))
            return elem

    return "존재하지 않습니다. 연산횟수는 {0}".format(op_cnt)

def binary_search(arr, target):
    first = 0
    last = len(arr)-1
    op_cnt = 0

    while first <= last:
        mid = ( first + last ) // 2
        op_cnt += 1
        if arr[mid] == target:
            print("연산 횟수는 {0}".format(op_cnt))
            return arr[mid]
        else:
            if arr[mid] > target:
                last = mid-1
            else:
                first = mid+1

    return "존재하지 않습니다. 연산횟수는 {0}".format(op_cnt)

if __name__ == "__main__":
    arr = [x for x in range()]

    # print(sequencial_search(arr, 88888))
    print(binary_search(arr, 88888))

    # print()
    # print("arr[80000] ({0})을 삭제합니다. ".format(arr[80000]))
    # del arr[80000]
    # print()

    # print(sequencial_search(arr, 80000))
    print(binary_search(arr, 5))

