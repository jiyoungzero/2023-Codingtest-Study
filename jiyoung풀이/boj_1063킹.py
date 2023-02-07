# 구현, 시뮬레이션, 21분~ 

import sys 
input = sys.stdin.readline

# ord 함수 기억하기 (문자 -> 십진수 변환)
# "A" : 65, "a" : 97

king_pos,stone_pos , n = map(str,(input().split()))
s = (int(stone_pos[1]), ord((stone_pos[0]))-64)
k = (int(king_pos[1]), ord((king_pos[0]))-64)
d = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"]
direction = {}
for a, b in zip(d, [(0,1),(0,-1),(-1,0),(1,0),(1,1),(1,-1),(-1,1),(-1,-1)]):
    direction[a] = b

# k = (2, 1) = A2
def in_range(x, y):
    return 1<= x <= 8 and 1<= y<= 8

for _ in range(int(n)):
    move = input().rstrip()
    nx, ny = k[0]+direction[move][0], k[1] + direction[move][1]
    if in_range(nx, ny):
        # 돌과 같은 곳이라면
        if nx == s[0] and ny == s[1]:
            if in_range(s[0]+direction[move][0], s[1]+direction[move][1]):
                s = (s[0]+direction[move][0], s[1]+direction[move][1])
                k = (nx, ny)
        else:
            k = (nx, ny)
    else:continue


print("".join([chr(k[1]+64),str(k[0])]))
print("".join([chr(s[1]+64),str(s[0])]))    

