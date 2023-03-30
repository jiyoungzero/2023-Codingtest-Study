# 삼성 코테 느낌 꼭 혼자서 풀어보기 

# 1. 같은 열, 행 중 (중간에 다른 숫자가 있으면 안됨) 같은 숫자 b가 있으면  
#    해당 위치의 숫자 b * 2, 현재 숫자 a 없애기 

# 2. 같은 열, 행 중 같은 숫자가 없으면
#    상, 하, 좌, 우 move시켜서 같은 숫자가 같은 행, 열에 위치하는지 check 

# 3. 1-2번 반복 5번까지

# 2 2 2    0 2 4       
# 4 4 4 -> 0 4 8   -> 
# 8 8 8    0 8 16
# 

import sys
from copy import deepcopy
input =sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
que = deque()
answer = 0

def move(direction):
    global arr
    # up
    if direction == 0: 
        for col in range(n):
            for row in range(n): # 한 줄 당 같은 숫자 있는지 체크
                if arr[row][col] != 0:
                    que.append(arr[row][col])
                    arr[row][col] = 0
            cur_row = 0    
            while que: 
                now_value = que.popleft()
                if now_value == arr[cur_row][col]: # 같은 숫자면 곱하기 2
                    arr[cur_row][col]*=2
                    cur_row += 1
                elif arr[cur_row][col] == 0: # 해당 위치가 아직 안채워져있으면
                    arr[cur_row][col] = now_value
                elif now_value != arr[cur_row][col]:
                    cur_row += 1
                    arr[cur_row][col] = now_value
                    
    # down
    if direction == 1:
        for col in range(n):
            for row in range(n-1, -1, -1): # 한 줄 당 같은 숫자 있는지 체크
                if arr[row][col] != 0:
                    que.append(arr[row][col])
                    arr[row][col] = 0
            cur_row = n-1    
            while que: 
                now_value = que.popleft()
                if now_value == arr[cur_row][col]: # 같은 숫자면 곱하기 2
                    arr[cur_row][col]*=2
                    cur_row -= 1
                elif arr[cur_row][col] == 0: # 해당 위치가 아직 안채워져있으면
                    arr[cur_row][col] = now_value
                elif now_value != arr[cur_row][col]:
                    cur_row -= 1
                    arr[cur_row][col] = now_value
    # right 오른쪽
    if direction == 2:
        for row in range(n):
            for col in range(n-1, -1, -1): # 한 줄 당 같은 숫자 있는지 체크
                if arr[row][col] != 0:
                    que.append(arr[row][col])
                    arr[row][col] = 0
            cur_col = n-1    
            while que: 
                now_value = que.popleft()
                if now_value == arr[row][cur_col]: # 같은 숫자면 곱하기 2
                    arr[row][cur_col]*=2
                    cur_col -= 1
                elif arr[row][cur_col] == 0: # 해당 위치가 아직 안채워져있으면
                    arr[row][cur_col] = now_value
                elif now_value != arr[row][cur_col]:
                    cur_col -= 1
                    arr[row][cur_col] = now_value
    # left 왼쪽
    if direction == 3:
        for row in range(n):
            for col in range(n): # 한 줄 당 같은 숫자 있는지 체크
                if arr[row][col] != 0:
                    que.append(arr[row][col])
                    arr[row][col] = 0
            cur_col = 0    
            while que: 
                now_value = que.popleft()
                if now_value == arr[row][cur_col]: # 같은 숫자면 곱하기 2
                    arr[row][cur_col]*=2
                    cur_col += 1
                elif arr[row][cur_col] == 0: # 해당 위치가 아직 안채워져있으면
                    arr[row][cur_col] = now_value
                elif now_value != arr[row][cur_col]:
                    cur_col += 1
                    arr[row][cur_col] = now_value
                    
                                        

def solution(cnt):
    global arr, answer
    if cnt == 5:
        answer = max(max(lst) for lst in arr)
        return answer
    
    cur_arr = deepcopy(arr)
    for k in range(4): #상하좌우 
        move(k)
        solution(cnt+1)
        arr = deepcopy(cur_arr)

print(solution(0))
    

