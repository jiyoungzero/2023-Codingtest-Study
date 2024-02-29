import sys
input = sys.stdin.readline 

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0 # 격자 밖으로 나간 모래의 양

# 왼쪽, 아래, 오른쪽, 위쪽
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]


def rotate_90(prop): # 반시계방향으로 회전
    rotated_prop = list(reversed(list(zip(*prop))))
    return rotated_prop