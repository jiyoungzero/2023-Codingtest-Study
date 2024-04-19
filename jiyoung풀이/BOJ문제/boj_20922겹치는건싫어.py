import sys
input = sys.stdin.readline 
from collections import defaultdict

n, k  = map(int, input().split())
arr = list(map(int ,input().split()))
s, e = 0, 0
answer = 0
num_cnt = defaultdict(int)

while e < n:
    if num_cnt[arr[e]] >= k:        
        num_cnt[arr[s]] -= 1
        s += 1

    else:
        num_cnt[arr[e]] += 1  
        e += 1
        answer = max((e-s), answer)  

print(answer)

        
    
    
    
        
        