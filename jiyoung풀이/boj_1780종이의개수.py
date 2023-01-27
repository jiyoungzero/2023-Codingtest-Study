import sys
input = sys.stdin.readline

n = int(input())
a_cnt, b_cnt, c_cnt = 0,0,0
arr = [list(map(int, input().split())) for _ in range(n)]

def paper(x, y, n):
    global a_cnt, b_cnt, c_cnt
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[x][y] != arr[i][j]:
                paper(x, y, n//3)
                paper(x, y+n//3, n//3)
                paper(x, y+2*n//3, n//3)
                
                paper(x+n//3, y, n//3)
                paper(x+n//3, y+n//3, n//3)
                paper(x+n//3, y+2*n//3, n//3)
                
                paper(x+2*n//3, y, n//3)
                paper(x+2*n//3, y+n//3, n//3)
                paper(x+2*n//3, y+2*n//3, n//3)
                return
            
    if arr[x][y] == -1:a_cnt+=1
    elif arr[x][y] == 0:b_cnt+=1
    else:c_cnt+=1
    
paper(0,0,n)
print(a_cnt)
print(b_cnt)
print(c_cnt)
