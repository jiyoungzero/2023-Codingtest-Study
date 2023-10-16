# 문제 스스로 풀어보기 

# 양 옆을 검사하고 현재 위치와 같은지, 다른 것을 넣고 다시 옆으로 
# 옮겨가고...순으로 해서 검사 

# paint, dfs 함수 2개 만들기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 
# 무한 루프..
# T = int(input().rstrip())
# dx, dy = [0,0,-1,1], [1,-1,0,0]

# def in_range(x, y):
#     global n
#     global m
#     return 0<=x<n and 0<=y<m

# # 격자점 색칠하는 함수
# def paint(x, y, nx, ny):
#     # 현재 위치랑 nx, ny이 같은 색이면
#     # 다른 색이면 --> ?이면, ?이 아니라면
#     global arr

#     if (arr[x][y] != "?" and arr[nx][ny] != "?") and arr[nx][ny] == arr[x][y]:
#         return False
    
#     elif(arr[nx][ny] != arr[x][y]) and arr[nx][ny] == "?":
#         if arr[x][y] == "." : arr[nx][ny] = "#"
#         else: arr[nx][ny] = "."
#         return True
    
#     elif (arr[nx][ny] != arr[x][y]) and arr[x][y] == "?":
#         if arr[nx][ny] == "." : arr[x][y] = "#"
#         else: arr[x][y] = "."
#         return True
    
#     elif (arr[nx][ny] != arr[x][y]) or (arr[x][y] == "?" and arr[nx][ny] == "?"):
#         return True
    

# def dfs(x, y, flag):
#     global n
#     global m
#     # 종료 조건 / 끝지점 
#     if flag == False:
#         return flag
#     if x == (n-1) and y == (m-1):
#         return flag
    
#     # 모든 배열을 돌면서 
#     for x in range(n):
#         for y in range(m):
#                 # 사방을 검사한 후 
#                 # (r, c)가 배열 내 범위라면
#                 # 색칠하고 넘어간다
#                 for i in range(4):
#                     nx, ny = x+dx[i], y+dy[i]
#                     if in_range(nx, ny):
#                         flag = paint(x, y, nx, ny)
#                     dfs(nx, ny, flag)

                
    

# for t in range(1, T+1):
#     n, m = tuple(map(int, input().split()))
    
#     arr = [list(map(str, input())) for _ in range(n)]
    
#     flag = dfs(0,0, True)

#     if flag : print(f"#{t} possible")
#     else: print(f"#{t} impossible")

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    board = [0, 0, 0, 0]
    
    # ?는 아무거나 상관없으므로 고려X
    for col in range(n):
        for row in range(m):
            
            if arr[col][row] == '#':
                if (col+row) % 2 == 0:
                    board[0] += 1
                elif (col+row) % 2 == 1:
                    board[1] += 1
                    
            elif arr[col][row] == '.':
                if (col + row) % 2 == 0:
                    board[2] += 1
                elif (col + row) % 2 == 1:
                    board[3] += 1

    if (board[0] and board[1]) or (board[2] and board[3]) or (board[0] and board[2]) or (board[1] and board[3]):
        answer = 'impossible'
    else:
        answer = 'possible'
        
    print(f"#{t+1}", answer)