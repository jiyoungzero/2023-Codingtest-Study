import sys
input = sys.stdin.readline 

n = int(input())
target = int(input())

arr = [[0]*n for _ in range(n)]
x, y = n//2, n//2
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
cnt = 0
arr[x][y] = 1
answer = [x, y]

def can_go(sx, sy):
    if sx < 0 or sy < 0 or n <= sx or n <= sy: return False
    if arr[sx][sy] > 0:return False
    return True

while True:
    if (x, y) == (0,0):break
    for k in range(4):
        if k == 0 or k == 2:
            cnt += 1
        for _ in range(cnt):
            nx, ny = x + dxs[k], y + dys[k]
            if can_go(nx, ny):
                arr[nx][ny] = arr[x][y] + 1

                x, y = nx, ny
                
for i in range(n):
    for j in range(n):
        if arr[i][j] == target:
            answer = [i, j]
        print(arr[i][j], end = " ")
    print()
print(*answer)
        
