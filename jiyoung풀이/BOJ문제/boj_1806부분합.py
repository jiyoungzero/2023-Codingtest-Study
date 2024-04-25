# 투포인터
import sys
input = sys.stdin.readline 

N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = int(1e9)
l, r = 0 ,0

sum_ = 0
while True:
    if sum_ >= S:
        answer = min(answer, (r-l))
        sum_ -= arr[l]
        l += 1    # print("합 = ", sum_, s, "(s, e) =", (s, e))
    elif sum_ < S:
        sum_ += arr[r]
        r += 1
    if r == N or l > r:break


print(answer if answer < int(1e9) else 0)
        
    
    
