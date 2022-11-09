#문제 스스로 풀어보기 15분
import sys
input = sys.stdin.readline

T = 10

# 회문인지 확인
def isword(lst):
    r_lst = []
    for i in range(len(lst)-1, -1, -1):
        r_lst.append(lst[i])

    if lst == r_lst:
        return True

def in_range(x):
    return 0<= x <= 8

def trans(a):
    n = len(a)
    m = len(a[0])
    new_a = [[0]*8 for _ in range(8)]
    for i in range(n):
        for j in range(m):
            new_a[j][n-i-1] = a[i][j]
    return new_a


for t in range(1, T+1):
    result = 0
    n = int(input())
    arr = [list(map(str, input().rstrip())) for _ in range(8)]
    arr_trans = trans(arr)
    
    for i in range(8):
        for j in range(8):
        # 행 검색
            if in_range(j+n) and isword(arr[i][j:j+n]):
                result += 1
        # 열 검색 
            if in_range(j+n) and isword(arr_trans[i][j:j+n]):
                result += 1
            

    print(f"#{t} {result}")