import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0


s, e= 0, 0
odd_cnt = 0
while True:
    if odd_cnt > k:
        if arr[s]%2 == 1:odd_cnt -= 1
        s += 1
    elif e == n:break
    else:
        if arr[e]%2 == 1:odd_cnt += 1
        e += 1
    
    if odd_cnt <= k:
        answer = max(answer, e-s-odd_cnt)
        
print(answer)
    
    
    
    

        