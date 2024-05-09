import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
answer = int(1e9)*2+1
arr.sort()

a, b = 0, 1
while a < b and b < n:
    sub = abs(arr[a] - arr[b])
    if sub >= m :
        answer = min(answer, sub)
        a += 1
        if a == b:
            b += 1
    else:
        b += 1
print(answer)