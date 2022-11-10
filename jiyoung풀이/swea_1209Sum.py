# 문제 스스로 풀어보기 5분
import sys
input = sys.stdin.readline

T = 10

def trans(a):
    n = len(a)
    m = len(a[0])
    new_a = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_a[j][n-i-1] = a[i][j]
    return new_a

for t in range(10):
    result = []
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    trans_arr = trans(arr)

    for i in range(100):
        result.append(sum(arr[i])) 
        result.append(sum(trans_arr[i]))
    
    # 대각선 \
    tmp = 0
    for i in range(100):
        tmp += arr[i][i]
    result.append(tmp)
    
    # 대각선 / 
    l, r, tmp2 = 0, 99, 0
    while l != 99:
        tmp2 += arr[l][r]
        l += 1
        r -= 1
    result.append(tmp2)
        
    
    print(f"#{n} {max(result)}")