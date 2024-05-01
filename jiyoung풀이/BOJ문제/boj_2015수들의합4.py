import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0]*n
prefix[0] =arr[0]
answer = 0

for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]
prefix = [0] + prefix

print(prefix)
for i in range(1, n+1):
    for j in range(i, n+1):
        if prefix[j] - prefix[i-1] == k:
            # print(i, j)
            answer += 1
print(answer)
    