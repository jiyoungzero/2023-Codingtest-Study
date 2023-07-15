# 구현

import sys
input = sys.stdin.readline

# k1 = (x+-2, y+-1), k2 = (x+-1, y+-2)

command = input()
x, y = int(command[1]), int(ord(command[0]))
move = [(2,1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
cnt = 0

def in_range(x, y):
    return 1<= x <= 8 and int(ord('a'))<= y<= int(ord('h'))

for m in move:
    a, b = m
    if in_range(x+a, y+b):
        cnt += 1
        
print(cnt)
