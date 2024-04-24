import sys
input = sys.stdin.readline 
from collections import defaultdict

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.extend(arr) # 원형이므로 2개를 이어준다

s, e = 0, 0
num_cnt = defaultdict(int)
answer = 0
num_cnt[c] += 1


# init
for i in range(k):
    num_cnt[arr[s+i]] += 1
e = k

while e <= n:
    answer = max(answer, len(num_cnt))
    
    num_cnt[arr[s]] -= 1
    if num_cnt[arr[s]] == 0:
        del num_cnt[arr[s]]
    s += 1
    
    num_cnt[arr[e]] += 1
    e += 1
print(answer)
    
    