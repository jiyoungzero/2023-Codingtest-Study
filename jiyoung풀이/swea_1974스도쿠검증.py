# 문제 스스로 풀어보기, 20분부터

import sys
input = sys.stdin.readline

T = int(input())

def isnot_success(s):
    global result
    if len(s) != 9:
        result = 0
        return


for t in range(1, T+1):
    # 이차원 배열로 입력 받아서 행/열 set의 개수가 9개가 되는지 검사
    arr =[ list(map(int, input().split())) for _ in range(9) ]
    result = 1
    
    c_set, r_set, block_set = set(), set(), set()
    

    for i in range(9):
        c_set, r_set = set(), set()
        for j in range(9):
            r_set.add(arr[i][j])
            c_set.add(arr[j][i])
        isnot_success(r_set)
        isnot_success(c_set)
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            block_set = set()
            for m in range(3):
                for n in range(3):
                    block_set.add(arr[i+m][j+n])
            isnot_success(block_set)
        

    print(f"#{t} {result}")