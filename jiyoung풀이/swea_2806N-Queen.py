#문제 스스로 풀어보기


# set까지는 생각했으나.. 다른 사람 풀이 참고함 , 30분 초과
import sys
input = sys.stdin.readline
# 모든 행, 열, 대각선 위에는 하나의 요소만 있어야 함 -> set


T = int(input().rstrip())

def is_nqueen(x):
    global result
    global n

    
    # l_diag = / , r_diag = \
    if x == n:
        result += 1
        return
    
    for i in range(n):
        if i in col or (i+x) in l_diag or (x-i) in r_diag: # 열, 두 대각선에 하나라도 존재하면 넘어가고
            continue
        
        # 아니면 경우의 수를 넣어주기
        col.add(i)
        l_diag.add(x+i)
        r_diag.add(x-i)
        is_nqueen(x+1)
        
        # 백트레킹
        col.remove(i)
        l_diag.remove(x+i)
        r_diag.remove(x-i)
        


for test_case in range(1, T+1):
    n = int(input())
    result = 0
    col, l_diag, r_diag = set(), set(), set()
    
    is_nqueen(0)
    
    print(f"#{test_case} {result}")