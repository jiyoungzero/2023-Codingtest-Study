import sys
input = sys.stdin.readline

n, m = map(int ,input().split())
tk = [int(input()) for _ in range(n)]


# 인원이 10**9 -> 그리디, 완전탐색(내가 생각한 거)는 시간초과
# 이분탐색으로 가자 -> 완탐을 거의 대체할 수 있다. 
l, r = min(tk), max(tk)*m
answer = r
while l <= r:
    mid = (l+r)//2
    total = 0
    for t in tk:
        total += (mid//t)
    
    if total >= m:
        answer = min(answer, mid)
        r = mid - 1
    else:
        l = mid +1 
        
print(answer)
        
            
    
