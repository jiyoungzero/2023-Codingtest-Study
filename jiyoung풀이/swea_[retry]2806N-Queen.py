# 다시 풀어보기

import sys
input = sys.stdin.readline


T = int(input())

def nqueen(r):

    global result
    if r == n:
        result += 1
        return result
    
    for c in range(n):
        if (c in col) or ((c+r) in r_diag ) or ((r-c) in l_diag):
            continue
        col.add(c)
        l_diag.add(r-c)
        r_diag.add(c+r)
        
        nqueen(r+1)
        
        col.remove(c)
        l_diag.remove(r-c)
        r_diag.remove(c+r)
    return result
    

for t in range(T):
    n = int(input())
    result = 0
    col, l_diag, r_diag = set(), set(), set()
    print(f"#{t+1} {nqueen(0)}")