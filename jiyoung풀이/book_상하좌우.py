# 구현 

# r = (0, 1) u = (-1, 0) d = (1, 0) l = (0, -1)
import sys
input = sys.stdin.readline

n = int(input())
command = list(map(str, input().split()))
start = [1,1]



for c in command:
    if start[1] != n and c == "R":
        start[1]+=1
    elif start[0] != 1 and  c == "U":
        start[0] -= 1
    elif start[0] != n and c == "D":
        start[0] += 1
    elif  start[1] != 1 and c == "L":
        start[1] -= 1

print(*start) # 리스트 한 줄에 한번에 출력하기 