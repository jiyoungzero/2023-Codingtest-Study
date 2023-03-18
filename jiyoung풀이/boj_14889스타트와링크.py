# 백트래킹

import sys
import itertools
input =sys.stdin.readline
# (2 + 1) + (5+1) +(5+3) = 3+6+8 = 17
# (3+2)+(4+2)+(4+4) = 5+6+8 =19
# (1, 3, 5) -> ((1,3), (3,1), (1,5),(5,1),(3,5),(5,3))
tmp = []

# 0      1      2        3 
# 0      1      2        3

def backtracking(depth, idx):
    global min_value
    if depth == n//2:
        start, link = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += (cost[i][j])
                elif not visited[i] and not visited[j]:
                    link += (cost[i][j])
        min_value = min(min_value, abs(start-link))
        return 

    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            backtracking(depth+1,i+1)
            visited[i] = False
            


n = int(input())
cost = []
min_value = int(1e9)
visited = [False]*n

for _ in range(n):
    cost.append(list(map(int, input().split())))
    
backtracking(0,0)
print(min_value)
    



    
    

