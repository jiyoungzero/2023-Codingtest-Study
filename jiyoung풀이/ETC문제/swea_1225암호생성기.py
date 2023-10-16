# 문제 스스로 풀어보기 45분 시작

import sys
input = sys.stdin.readline
# 20분소요
def cycle(arr):
    for i in range(1,6):
        front = arr[0]
        del arr[0]
        if front-i <= 0:
            arr.append(0)
            return False
        arr.append(front - i)
    return True 

def password(arr):
    flag = True
    while flag:
        flag = cycle(arr)
    return arr

for _ in range(10):
    t = int(input())
    result = []
    arr = list(map(int, input().split()))
    
    arr = password(arr)
    
    
    print(f"#{t}", end=" ")
    for ele in arr:
        print(ele, end=" ")