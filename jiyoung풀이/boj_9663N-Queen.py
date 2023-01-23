# 구현?
import sys
input = sys.stdin.readline

n = int(input())
row = [0] * n
result = 0

def flag(x):
    # 행 row[i], 열 j  --> abs(row[x] - row[i]) == abs(x - i):
    for i in range(x):
        if (row[i] == row[x]) or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def nqueen(x):
    global result
    if x == n:
        result += 1
        return
    else:
        for j in range(n):
            row[x] = j
            if flag(x):
                nqueen(x+1)
                
nqueen(0)
print(result)
    
        
    

