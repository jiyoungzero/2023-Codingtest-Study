# 구현?
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = [[0]*n for _ in range(n)] # 가능 0, 이미 차있음 1
result = 0

def put(pos,num):
    row, col = pos
    for i in range(n): # 행, 열
        arr[row][i] = num
        arr[i][col] = num
    for i in range(n): # 대각선 
        for j in range(n):
            if i-j == 0 or i+j == (n-1):
                arr[i][j] = num

def nqueen(x):
    global result
    if x == n:
        result += 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                put((i, j), 1) # 채우고
                x += 1
                nqueen(x)
                put((i,j), 0) # 다시 원래대로
                
nqueen(0)
print(result)
    
        
    

