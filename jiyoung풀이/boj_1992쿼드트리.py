# 분할 정복 

import sys
input = sys.stdin.readline


n = int(input())
arr = []
result = ""
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))
    
def quadtree(row, col, n):
    global result 
    
    if n!=1:
        for i in range(row, row+n):
            for j in range(col, col+n):
                if arr[row][col] != arr[i][j]:
                    result += "("
                    quadtree(row, col, n//2)
                    quadtree(row,col+n//2, n//2)
                    quadtree(row+n//2,col, n//2)
                    quadtree(row+n//2,col+n//2, n//2)
                    result += ")"
                    return
    if arr[row][col] == 1:
        result += "1"
    else:
        result += "0"
                
quadtree(0,0,n)
print(result)
