# hash, 그래프 탐색 

# 아기상어랑 비슷한 흐름 : 한 번 흐름에 필요한 함수가 2개 
# import sys
# from collections import deque
# input = sys.stdin.readline 

# arr = []
# x, y = 0, 0
# for i in range(3):
#     lst = list(map(int, input().split()))
#     arr.append(lst)
#     for idx, ele in enumerate(lst):
#         if ele == 0:
#             x, y = i, idx # 0 위치
            
# dxs, dys = [0,0,1,-1],[1,-1,0,0]
# asc_arr = [[1,2,3],[4,5,6],[7,8,0]]
# visited = [[False]*(3) for _ in range(3)]

# def isAsc(a):
#     return asc_arr == a

# # 0주변 숫자만 최소로 추가하는 함수 
# def bfs(start_x, start_y):
#     que = deque((start_x, start_y))
#     visited[start_x][start_y] = True
#     tmp = []
#     while que:
#         x, y = que.popleft()
        
#         for k in range(4):
#             nx, ny = x + dxs[k], y+dys[k]
#             if 0<=nx<3 and 0<=ny<3:
#                 if not visited[nx][ny]:
#                     tmp.append((nx,ny,arr[nx][ny])) # 주변의 위치, 값
#                     que.append((nx, ny))
#                     # switch되어야 visited가 true 
#     return tmp.sort()

# # 바꿀 위치를 찾는 함수 
# def find(tmp):
#     flag = False
#     if len(tmp) == 1: return -1 #바꿀 수 있는 것이 없을 때 
    
#     for i in range(1,len(tmp)):
#         if tmp[i-1][2]+1 == tmp[i][2]:
#             flag = True
#         else:
#             del tmp[i]
            
#     if not flag:
#         return -1 #바꿀 수 있는 것이 없을 때 
#     elif flag:
#         if len(tmp) == 4:
#             return -1
#         elif len(tmp) == 3:
#             return tmp[1]
#         elif len(tmp) == 2:
#             return tmp[1]
#         else:
#             return -1
        
# count = 0
# while isAsc(arr) != True:
#     tmp = bfs(x, y)
#     result = find(tmp)
#     if result == -1:
#         print(-1)
#     else:
#         switch_x, switch_y = result[0], result[1]
#         o_x, o_y = x, y
#         x, y = switch_x, switch_y
#         switch_x, switch_y = o_x, o_y
#         count += 1
# print(count)
    
    
# 문자열을 123456789로 (0은 9로 바꾸는 전처리) sort한다는 생각으로 해야 시간초과가 안남(즉, 문자열 문제)
# visited는 해당 인덱스를 보는 것이 아니라, 그 배열 형태 자체를 봄 -> map 사용 {"배열" : "움직인 횟수"}

from collections import deque
import sys
input = sys.stdin.readline

arr = ""
for i in range(3):
    arr += "".join(list(map(str, input().split())))
    
dxs, dys = [0,0,1,-1],[1,-1,0,0]
visited = {arr:0}

def bfs(start_arr):
    que = deque([start_arr])
    while que:
        arr = que.popleft()
        cnt = visited[arr]
        z_idx = arr.index('0')
        
        if arr == "123456780":
            return cnt
        
        # 1차원 문자열 index -> 2차원 배열 index
        x = z_idx // 3
        y = z_idx % 3
        
        cnt += 1
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if 0<=nx<3 and 0<=ny<3:
                nz_idx = nx * 3 + ny # 2차원 배열 index -> 1차원 문자열 index
                # 문자열은 스위치가 힘들어서 리스트로 먼저 전환 
                arr_list = list(arr)
                arr_list[nz_idx], arr_list[z_idx] = arr_list[z_idx],arr_list[nz_idx]
                
                # 다시 문자열로 되돌리기
                new_arr = "".join(arr_list)
                
                if visited.get(new_arr) == None:
                    que.append(new_arr)
                    visited[new_arr] = cnt

    return -1

print(bfs(arr))                
        

    