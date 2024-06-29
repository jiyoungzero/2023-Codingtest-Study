import sys
input = sys.stdin.readline 

R, C, K = map(int, input().split())

dxs, dys = [-1,0,1,0],[0,1,0,-1] # 위, 오른쪽, 아래, 왼쪽 
fairies = [tuple(map(int, input().split())) for _ in range(K)] # (출발열, 출구방향)
answer = 0 # 행의 누적합

def in_range(x, y):
    return 0 <= x < 6 and 0 <= y < 5
    
def can_go_left(sx, sy): # 요정의 위치
    pass