from timeit import default_timer as timer

def factorial(n, op_cnt):

    if(n == 0):
        print("재귀함수 팩토리얼의 연산횟수는 ", op_cnt)
        return 1
    else:
        op_cnt += 1
        return n * factorial(n-1, op_cnt)

def factorial2(n):
    op_cnt = 0
    result = 1
    for x in reversed(range(1, n+1)):
        op_cnt += 1
        result = result * x

    print("반복문 팩토리얼의 연산횟수는 ", op_cnt)

    return result

start = timer()
print(factorial(300, 0))
fac_t = timer() - start
print(float(fac_t*60/1000), "\n")

start = timer()
print(factorial2(300))
fac2_t = timer() - start
print(str(fac2_t*60/1000), "\n")

import sys
print("반복문 Factorial이 재귀함수 Factorial보다 {0}배 빠르다 !".format(fac_t/fac2_t))

