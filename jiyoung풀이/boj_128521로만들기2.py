# dp

import sys
input =sys.stdin.readline
INF = int(1e6)
n = int(input())

# (2나 3으로 나누어 떨어지면 나누기) and (-1했을때 2나 3의 제곱근 == false)
# -1했을 때 제곱근이면 -1
# 2와 3으로 나누어떨어지지 않으면 -1하기 

# 제곱근인지 확인하는 함수
def isPow(target, num):
    flag = True
    while flag:
        tmp = target % num
        if tmp != 0:
            flag = False
            break
        target /= num
    return flag

while n>1:
    if isPow(n, 2) or isPow(n,3):
        print(n-1, end=" ")
        n -= 1
    elif not isPow(n-1, 2) and not isPow(n-1,3):
        if n%2==0:
            print(n//2, end=" ")
            n//=2
        elif n%3==0:
            print(n//3, end=" ")
            n//=3
    elif (n%2 != 0) and (n%3 != 0):
        print(n-1, end=" ")
        n-=1

