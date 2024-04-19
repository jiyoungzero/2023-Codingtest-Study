import sys
input = sys.stdin.readline 
from collections import defaultdict

n, k  = map(int, input().split())
arr = list(map(int ,input().split()))
s, e = 0, 0
answer = 0
num_cnt = defaultdict(int)
num_cnt[arr[s]] += 1

def check():
    for v in num_cnt.values():
        if v > k:
            return True
    return False

while e < n-1:
    if not check():
        e += 1
        num_cnt[arr[e]] += 1
    else:
        print(s, e, answer)
        answer = max((e-s), answer)        

        num_cnt[arr[s]] -= 1
        s += 1
print(answer)

        
    
    
    
        
        