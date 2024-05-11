import sys
input = sys.stdin.readline 

n = int(input())
arr = input().rstrip()
answer = 0

s, e = 0, 1
cnt = 1
while s < e and e < len(arr):
    if arr[e-1] != arr[e]:
        cnt += 1
    if cnt > n:
        answer = max(answer, (e-s+1))
        if arr[s] != arr[e]:
            cnt -= 1
        s += 1
    else:
        answer = max(answer, (e-s+1))
        e += 1
        
print(answer)
        
