# backtracking

import sys
input =sys.stdin.readline
from itertools import combinations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
lst = list(combinations([i for i in range(1, n+1)], n//2))
all = len(lst)
answer = int(1e9)

for i in range(all//2+1):
    s_score, e_score = 0,0
    s_t, e_t = lst[i], lst[all-i-1]
    s_lst, e_lst = list(combinations(s_t,2)), list(combinations(e_t,2))

    # 스타트 팀 계산
    for ele in s_lst:
        a, b = ele[0]-1, ele[1]-1
        s_score += arr[a][b] 
        s_score += arr[b][a]
        
    # end 팀 계산
    for ele in e_lst:
        a, b = ele[0]-1, ele[1]-1
        e_score += arr[a][b] 
        e_score += arr[b][a]
    
    answer = min(answer, abs(s_score-e_score))
    
print(answer)
        
    