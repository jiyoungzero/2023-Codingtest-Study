import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cmds = [list(map(int, input().split())) for _ in range(m)]
prefix = [0]*(len(arr)+1)

for cmd in cmds:
    a, b, k = cmd
    prefix[a-1] += k
    prefix[b] -= k

dp = [0]*(len(arr)+1)
dp[0] = prefix[0]
for i in range(1, len(arr)+1):
    dp[i] = dp[i-1] + prefix[i]

answer = []
for i in range(len(arr)):
    answer.append(arr[i]+dp[i])
print(*answer)
