import sys, copy
input = sys.stdin.readline

# 상어의 이동방향 
#   1. 아무 냄새가 없는 곳
#   2. 자신의 냄새가 있는 곳(특정한 우선순위에 따라 정함 (여러개일 시))

# 한 칸에 여러 상어가 있을 시 : 가장 작은 번호만 살아남음
BLANK = 0
answer = 0
dxs, dys = [-1,1,0,0],[0,0,-1,1] # 위, 아래, 왼쪽, 오른쪽
n, m, k = map(int, input().split())
arr = [] # 상어(상어의 번호, 상어의 방향 상태), 빈칸(0)
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
sharks = list(map(int, input().split()))
for i in range(len(sharks)):
    sharks[i] -= 1 # 각 상어들의 초기 방향 상태
    
# arr에 상어의 초기 방향 상태 저장 
for i in range(n):
    for j in range(n):
        if arr[i][j] != BLANK:
            shark_num = arr[i][j]-1
            shark_dir = sharks[shark_num]
            arr[i][j] = (shark_num, shark_dir)
                
dir_priorities = [] # 각 상어들의 방향 우선순위 
for _ in range(m):
    tmp = dict()
    for dir in range(4):
        a, b, c, d = map(int, input().split())
        tmp[dir] = [a-1, b-1, c-1, d-1]
    dir_priorities.append(tmp)

def only_survived_first():
    for i in range(n):
        for j in range(n):
            if arr[i][j] != BLANK:
                shark_num, _ = arr[i][j]
                if shark_num != 0:
                    return False
    return True

def save_smell():
    global smell_arr
    for i in range(n):
        for j in range(n):
            if arr[i][j] != BLANK:
                shark_num, _ = arr[i][j]
                smell_arr[i][j] = [shark_num, k]

def update_smell():
    for i in range(n):
        for j in range(n):
            if smell_arr[i][j] != -1:
                smell_arr[i][j][1] -= 1
                if smell_arr[i][j][1] == 0: # k시간이 다 지나면
                    smell_arr[i][j] = -1 # 빈칸으로

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(i, j, now_num, now_dir):
    ni, nj, nxt_dir = 0, 0 ,0
    can_go_lst = []
    # 이동할 수 있는 모든 상하좌우 중의 위치를 저장
    dir_priority = dir_priorities[now_num]
    for d in dir_priority[now_dir]:
        nx, ny = i + dxs[d], j + dys[d]
        if not in_range(nx, ny):
            continue
        if smell_arr[nx][ny] == -1:
            can_go_lst.append((nx, ny, d))
            return nx, ny, d
        if smell_arr[nx][ny] != -1 and smell_arr[nx][ny][0] == now_num:
            can_go_lst.append((nx, ny, d))
    
    ni, nj, nxt_dir = can_go_lst[0]
    return ni, nj, nxt_dir
    

def move_all():
    global arr
    nxt_arr = [[[] for _ in range(n)] for _ in range(n)] # 상어가 모두 이동한 이후의 배열
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] != BLANK:
                shark_num, shark_dir = arr[i][j]
                ni, nj, nxt_dir = move(i,j, shark_num, shark_dir)
                nxt_arr[ni][nj].append((shark_num, nxt_dir))
    
    # nxt_arr에서 원본 배열로 복사
    for i in range(n):
        for j in range(n):
            if len(nxt_arr[i][j]) > 1: # 여러 상어가 겹친 경우
                nxt_arr[i][j].sort()
                arr[i][j] = nxt_arr[i][j][0]
            elif len(nxt_arr[i][j]) == 1: # 한 마리 상어만 있는 경우
                arr[i][j] = nxt_arr[i][j][0]
            else: # 빈칸인 경우
                arr[i][j] = BLANK


smell_arr = [[-1]*n for _ in range(n)] # 냄새 관리용 배열 아자잣    
while True:
    if only_survived_first() or answer > 1000:
        # for row in arr:
        #     print(*row)
        break
    
    # 현재 위치 냄새 남기기
    save_smell()
    
    # 모든 상어 이동시키기
    move_all()
    
    # k번 이동 후의 냄새 업데이트
    update_smell()
    
    answer += 1


print(answer if answer <= 1000 else -1)
    
    

