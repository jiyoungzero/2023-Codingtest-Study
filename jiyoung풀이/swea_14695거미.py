# 문제 스스로 풀어보기 

import sys
# import numpy as np # 모듈 사용 안됨
input = sys.stdin.readline

T = int(input())

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

# 3차원으로 된 점의 개수가 한 평면상에 있는지 판단해야 함  -> np.cross
def fly(v):
    global flag
    # 평면의 법선벡터를 구하기 위해 벡터 a, b 구하기
    a = [v[0][0] - v[1][0], v[0][1] - v[1][1],v[0][2] - v[1][2]]
    b = [v[1][0] - v[2][0], v[1][1] - v[2][1],v[1][2] - v[2][2]]
    v_90 = cross(a, b)
    ans = []
    
    # 평면방정식 y = v_90[0]x1 + v_90[1]x2 + v_90[2]x3
    for i in v:
        tmp = 0 
        for j in range(3):
            tmp += i[j]*v_90[j]
        ans.append(tmp)

    if len(set(ans)) == 1: return True
    else : return False

for t in range(T):
    flag = True
    n = int(input())
    
    v = [list(map(int, input().split())) for _ in range(n)]
    flag = fly(v)
    
    if flag == True : result = "TAK"
    else: result = "NIE"
    print(f"#{t+1} {result}")
    
    # 정답은 맞는데 런타임에러로 오답처리