# 투 포인터
import sys
input =sys.stdin.readline


n, m  = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
arr.sort() # 1 1 1 2 2 2 3 3 4 5
print(arr)

for i in range(n-1):
    for j in range(i+1, n+1):
        target = sum(arr[i:j])
        if target > m:
            break
        elif target == m:
            answer += 1
print(answer)
