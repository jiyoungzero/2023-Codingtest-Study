# dfs


# 동시다발적으로 전파 + 전파 시 우선순위가 있을 경우

import sys
import copy
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
s, x, y = map(int, input().split())
dxs, dys = [0,0,1,-1], [1,-1,0,0]

# 이미 있는 바이러스와 비교를 위해
real_arr = copy.deepcopy(arr)
# 바이러스 후의 배열
temp = copy.deepcopy(arr)

time = 0
def in_range(x, y):
    return 0<=x<n and 0<=y<n

def virus(x, y):
    for i in range(4):
        nx, ny = x +dxs[i], y+dys[i]
        if (in_range(nx, ny) and temp[nx][ny] == 0) or (in_range(nx, ny) and temp[nx][ny] > arr[x][y]):
            if real_arr[nx][ny] == 0: temp[nx][ny] = arr[x][y]
            
def dfs(time):
    if time == s:return
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                virus(i, j)
    time += 1
    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]
    dfs(time)
                

dfs(time)
print(temp[x-1][y-1])