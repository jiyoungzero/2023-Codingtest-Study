import sys
input = sys.stdin.readline 

n, m, h, k = map(int ,input().split())
tmp = [tuple(map(int ,input().split())) for _ in range(m)] # (x, y, d)
runners = dict()
for i, (x, y, d) in enumerate(tmp):
    runners[i] = [x-1, y-1, d, 0, False] 
dirs = {1 : [(0,1),(0,-1)], 2: [(1,0),(-1,0)]}# d == 1 : 우, 좌, d == 2 : 하, 상

trees = [ ]
for _ in range(h):
    tx, ty = tuple(map(int, input().split()))
    trees.append((tx - 1, ty - 1))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def close2catcher(x, y):
    return (abs(catcher[0] - x) + abs(catcher[1] - y)) <= 3

# 도망자의 위치가 겹쳐질 수 있다! + 다 동시에 움직임
def move_runners():
    for key, runner in runners.items():
        x, y, d, d_idx, catched = runner
        if catched:continue
        if not close2catcher(x, y):continue
        dxs, dys = dirs[d][d_idx]
        nx, ny = x + dxs, y + dys

        if not in_range(nx, ny):
            d_idx = (d_idx + 1)%2
            dxs, dys = dirs[d][d_idx]
            nx, ny = x + dxs, y + dys
            if [nx, ny] != catcher:
                runners[key] = (nx, ny, d, d_idx, catched)
            else:
                runners[key] = (x, y, d, d_idx, catched)
        else:
            if [nx, ny] == catcher:continue
            else: runners[key] = (nx, ny, d, d_idx, catched)

def catcher_path(): # 달팽이 모양
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 상, 좌, 하, 우
    path = [(n//2, n//2, 0)] 
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    
    visited[n//2][n//2] = True
    cur_x, cur_y = n//2, n//2
    while True:
        if (cur_x, cur_y) == (n-1,0):break
        for dir in range(4):
            if dir == 0 or dir == 2:
                cnt += 1
            for _ in range(cnt-1):
                nx = cur_x + dxs[dir]
                ny = cur_y + dys[dir]
                if not in_range(nx, ny):continue
                if visited[nx][ny]: continue

                path.append((nx, ny, dir))
                visited[nx][ny] = True
                cur_x, cur_y = nx, ny

            nx = cur_x + dxs[dir]
            ny = cur_y + dys[dir]
            if not in_range(nx, ny):continue
            if visited[nx][ny]: continue

            visited[nx][ny] = True
            cur_x, cur_y = nx, ny
            
            # 마지막에는 방향을 틀은 상태로 저장
            path.append((cur_x, cur_y, (dir + 1)%4))
    for i in range(n-2, 0, -1):
        path.append((i, 0, 0))
    path.append((0,0,2))
    
    prev_d = path[0][2]
    reverse_path = []
    for x, y, d in path[1:-1]:
        if d != prev_d:
            reverse_path.append((x, y, (d+1)%4))
        else:
            reverse_path.append((x, y, (d+2)%4))
        prev_d = d
        
    path += reverse_path[::-1]
    path.append((0,0,0))
    return path[1:]
        
def catch(sx, sy, catch_dir):
    # 해당 방향으로 배열 3칸까지 확인 : 도망자 잡기, 나무가 있는 곳만 확인 불가
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    result = 0
    lst = [(sx, sy)]
    for _ in range(2):
        nx, ny = sx + dxs[catch_dir], sy+ dys[catch_dir]
        if not in_range(nx, ny):continue
        lst.append((nx, ny))
        sx, sy = nx, ny

    for x, y in lst:
        if (x, y) in trees:continue
        for key, runner in runners.items():
            rx, ry, d, d_idx, catched = runner
            if catched : continue
            if (x, y) == (rx, ry):
                # print('catcher = ',catcher, runner)
                result += 1
                runners[key] = [rx, ry, d, d_idx, True]

    return result

path = catcher_path()
catch_idx = 0
answer = 0
catcher = [n//2, n//2]
for t in range(1, k+1):
    # print(t, "턴 ", "이동 전 술래 위치 = ", catcher)
    arr = [[0]*n for _ in range(n)]
    move_runners()

    cx, cy, cd = path[catch_idx]
    catcher = [cx, cy]
    
    catch_cnt = catch(cx, cy, cd)

    answer += t*catch_cnt

    catch_idx += 1
    catch_idx %= len(path)
    # print(t, "턴 -> 이동 후 술래 위치", catcher)
    # print(runners)
    # print()


# for i, p in enumerate(path):
#     print(i+1, p)
print(answer)