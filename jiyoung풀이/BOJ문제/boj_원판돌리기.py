# 구현 + deque rotate
from collections import deque 
import copy
n, m, t = map(int, input().split())
circles = []
for _ in range(n):
    circles.append(list(map(int, input().split())))

cmds = [list(map(int, input().split())) for _ in range(t)]

# x, d, k : x의 배수인 원판을 d방향으로 k칸 회전 (d == 0:시계)
# 인접 + 같은 수 -> 지우기
# 없는 경우 : 원판의 평균을 구한 후, 평균보다 크면 -1, 작으면 +1
answer = 0 # 원판에 적힌 수의 합 

# shift right : que.rotate(1)
# shift left : que.rotate(-1)

dxs, dys = [0,0,1,-1],[1,-1,0,0]

def rotate_circle(x, d, k):
    check_sum = 0
    for i in range(1, n+1):
        if (i+1)%x == 0: # 회전시킬 원반
            check_sum += sum(circles[i]) # 남아있는 수가 있는지 확인 
            if d == 0:
                que = deque(circles[i])
                que.rotate(k)
                circles[i] = list(que)
            else:
                que = deque(circles[i])
                que.rotate(-k)
                circles[i] = list(que)
    return check_sum


def bfs(i,j):
    que = deque()
    que.append((i,j))
    visited[i][j] = True
    
    target_num = circles[i][j]
    circles[i][j] = 0
    cnt = 0
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if 0 > ny or m <= ny:
                if y == 0:
                    ny = m-1
                elif y == (m-1):
                    ny = 0
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if circles[nx][ny] == target_num:
                        cnt += 1
                        circles[nx][ny] = 0 # 지우기
                        visited[nx][ny] = True
                        que.append((nx, ny))
    if cnt == 0:
        circles[i][j] = target_num
    return cnt
                
    

def get_answer():
    global answer
    for ele in circles:
        answer += sum(ele)

def change_by_avg():
    sum_value = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            sum_value += circles[i][j]
            if circles[i][j] > 0:
                cnt += 1

    avg = sum_value / cnt
    for i in range(n):
        for j in range(m):
            if circles[i][j] > 0:
                if circles[i][j] < avg:
                    circles[i][j] += 1
                elif circles[i][j] > avg:
                    circles[i][j] -= 1
                    

for cmd in cmds:
    x, d, k = cmd
    check_sum = 0
    
    check_sum = rotate_circle(x, d, k)
    if check_sum == 0:
        break
    
    visited = [[False]*m for _ in range(n)]
    same_num_cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and circles[i][j] != 0:
                same_num_cnt += bfs(i,j)
    if same_num_cnt == 0:
        change_by_avg()


    
get_answer()
print(answer)

