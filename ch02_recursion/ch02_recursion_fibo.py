from timeit import default_timer as timer

def fibo1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo1(n-2) + fibo1(n-1)

if __name__ == "__main__":
    start = timer()
    print(fibo1(30))
    fibo1_t = timer() - start
    print(fibo1_t)

# fibo(n)의 문제점.. fibo(9)가 호출되면 fibo(7) + fibo(8)이 호출된다.
# fibo(7)이 호출되고 재귀적으로 fibo(7)의 값이 반환될 것이다.
# fibo(8)이 호출되면 fibo(6) + fibo(7)이 호출된다.
# 근데, 여기서 또 fibo(7)이 호출된다.
# 앞서 fibo(7)의 값을 재귀적으로 구했음에도 다시 fibo(7)을 호출한다.
# 또 fibo(9)에서도 마찬가지로 그렇게 될 것이다.
# 피보나치 수열을 구하는 문제는 반복문을 이용하면 그 문제를 해결할 수 있다 !

def fibo2(n):
    arr = [0 for x in range(0, n)]

    for i, x in enumerate(arr):
        if i == 0:
            arr[i] = 0
        elif i == 1:
            arr[i] = 1
        else:
            arr[i] = arr[i-2] + arr[i-1]

    return arr[n-1]

if __name__ == "__main__":
    start = timer()
    fibo2_t = timer() - start
    print(fibo2(30))
    print(fibo2_t, "\n")

    print("피보나치 수열의 30번째 숫자를 구하는 것은 재귀함수보다 반복문으로 푸는 것이 {0}배는 빠르다 ! \n\n".format(fibo1_t/fibo2_t))


table = {'0': 0, '1': 1}

def fibo3(n):
    key = str(n-1)

    if key not in table :
        table[key] = fibo3(n-2) + fibo3(n-1)

    return table[key]

if __name__ == "__main__":
    start = timer()
    fibo3_t = timer() - start
    print(fibo3(30))
    print(fibo3_t, "\n")

    print("동적계획법으로 풀면 {0}배나 빠르다 !".format(fibo1_t/fibo3_t))
