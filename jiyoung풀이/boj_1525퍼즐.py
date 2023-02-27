# hash, 그래프 탐색 

# 아기상어랑 비슷한 흐름 : 한 번 흐름에 필요한 함수가 2개 
import sys
from collections import deque
input = sys.stdin.readline 

arr = []
x, y = 0, 0
for i in range(3):
    lst = list(map(int, input().split()))
    arr.append(lst)
    for idx, ele in enumerate(lst):
        if ele == 0:
            x, y = i, idx # 0 위치
            
dxs, dys = [0,0,1,-1],[1,-1,0,0]
asc_arr = [[1,2,3],[4,5,6],[7,8,0]]
visited = [[False]*(3) for _ in range(3)]

def isAsc(a):
    return asc_arr == a

# 0주변 숫자만 최소로 추가하는 함수 
def bfs(start_x, start_y):
    que = deque((start_x, start_y))
    visited[start_x][start_y] = True
    tmp = []
    while que:
        x, y = que.popleft()
        
        for k in range(4):
            nx, ny = x + dxs[k], y+dys[k]
            if 0<=nx<3 and 0<=ny<3:
                if not visited[nx][ny]:
                    tmp.append((nx,ny,arr[nx][ny])) # 주변의 위치, 값
                    que.append((nx, ny))
                    # switch되어야 visited가 true 
    return tmp.sort()

# 바꿀 위치를 찾는 함수 
def find(tmp):
    flag = False
    if len(tmp) == 1: return -1 #바꿀 수 있는 것이 없을 때 
    
    for i in range(1,len(tmp)):
        if tmp[i-1][2]+1 == tmp[i][2]:
            flag = True
        else:
            del tmp[i]
            
    if not flag:
        return -1 #바꿀 수 있는 것이 없을 때 
    elif flag:
        if len(tmp) == 4:
            return -1
        elif len(tmp) == 3:
            return tmp[1]
        elif len(tmp) == 2:
            return tmp[1]
        else:
            return -1
        
count = 0
while isAsc(arr) != True:
    tmp = bfs(x, y)
    result = find(tmp)
    if result == -1:
        print(-1)
    else:
        switch_x, switch_y = result[0], result[1]
        o_x, o_y = x, y
        x, y = switch_x, switch_y
        switch_x, switch_y = o_x, o_y
        count += 1
print(count)
    