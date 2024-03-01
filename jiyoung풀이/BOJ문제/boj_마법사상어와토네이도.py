import sys
input = sys.stdin.readline 

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = n//2, n//2
answer = 0 # 격자 밖으로 나간 모래의 양


# 왼쪽, 아래, 오른쪽, 위쪽
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
p1 = [[-2, 0, 0.02], [2, 0, 0.02], [-1,-1,0.1], [-1, 0, 0.07],[-1, 1, 0.01], [1, -1, 0.1], [1, 0, 0.07], [1, 1, 0.01], [0, -2, 0.05], [0, -1, 0]]
p2 = [[-y, x, z] for [x, y, z] in p1]
p3 = [[x, -y, z] for [x, y, z] in p1]
p4 = [[-x, y, z] for [x, y, z] in p2]

props = [p1, p2, p3, p4]
def move(cnt, dir):
    global answer, r, c
    for _ in range(cnt+1):
        r += dxs[dir] 
        c += dys[dir]
        if r < 0 or c < 0: # (0,0)에 이미 도착한 경우
            return
        
        # 모래 퍼트리기
        spread_sand = 0
        for dx, dy, rate in props[dir]:
            nr, nc = r + dx, c + dy
            if rate == 0:
                sand = arr[r][c] - spread_sand
            else:
                sand = int(arr[r][c]*rate)
            
            if 0 <= nr < n and 0 <= nc < n:
                arr[nr][nc] += sand
            else:
                answer += sand
            spread_sand += sand


def simulate():
    for i in range(n):
        if i%2 == 0:
            move(i, 0) # 좌
            if r == 0 and c == 0:
                break
            move(i, 1) # 하
        else:
            move(i, 2) # 우
            move(i, 3) # 상

simulate()         
print(answer)
        
    
    
