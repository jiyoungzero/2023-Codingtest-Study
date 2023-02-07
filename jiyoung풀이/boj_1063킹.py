# 구현, 시뮬레이션, 21분~ 

import sys 
input = sys.stdin.readline

# ord 함수 기억하기 (문자 -> 십진수 변환)
# "A" : 65, "a" : 97

stone_pos, king_pos, n = map(str,(input().split()))
s = (int(stone_pos[1]), ord((stone_pos[0]))-64)
k = (int(king_pos[1]), ord((king_pos[0]))-64)
d = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"]
direction = dict()
for a, b in zip(direction, [(0,1),(-1,0),(1,0),(-1,0),(-1,1),(-1,-1),(1,1),(1,-1)]):
    direction[a] = b
    
for _ in range(int(n)):
    move = input()
    nx, ny = 
    
    

