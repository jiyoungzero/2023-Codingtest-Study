# 0인지 체크함수
# 한자리수 체크 함수
# max값을 받아서 max가 1이 될때까지만 할까?
from collections import deque


def zeroCheck(a):
    if a <= 0:
        return True
    return False


for tc in range(1, 10+1):
    t = int(input())
    arr = deque(map(int, input().split()))
    m = max(arr)

    flag = 1
    while (flag):
        for i in range(1, 6):
            temp = arr.popleft() - i
            if zeroCheck(temp):
                arr.append(0)
                flag = 0
                break
            arr.append(temp)
    print("#{}".format(tc), end=" ")
    for a in arr:
        print("{}".format(a), end=" ")
    print()
