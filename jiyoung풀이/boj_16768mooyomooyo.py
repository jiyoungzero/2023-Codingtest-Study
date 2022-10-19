# 문제 스스로 풀어보기 

# 애니팡 같은 문제... -> 같은 공간에 있다. --> 아까 그 유기농배추 처럼 한 뭉탱이를 계산 한다.

# 한 뭉탱이가 K개 이상일 경우, 없애고 빈칸은 모두 0처리
# 위에 있는 중력에 의해 내려오는 것은 코드로 어떻게 구현할까...
# 함수롤 모듈화 하면 좋을 것 같다 
# 1. in_range()
# 2. K개 이상의 뭉탱이인지 판별 -> is_upperK()
# 3. 탐색 dfs함수 
# 4. 중력에 의해 0이 아닌 숫자들을 내려오게 하는 함수 --> gravity()


# 50분 초과 -> 풀이 참조함 
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = []
dxs, dys = [0,0,1,-1], [1,-1,0,0]
cnt = 0 # 뭉탱이의 개수 

lst = [list(input()) for _ in range(n)]
    
def in_range(x,y):
    return 0<=x<n and 0<=y<10

# 열단위로 0이 있으면 한칸 아래로 내리 --> 왜 열단위로?? 아래로 내리는 것이기 때문에 밑에 0이 있는 자리까지 알아야 코드가 쉽다
# 
def gravity(lst):
    for c in range(10):
        temp = [] # 열을 저장한 리스트
        cnt = 0 # 0이 나온 횟수
        for r in range(n):
            if lst[r][c] != 0:
                temp.append(lst[r][c])
                lst[r][c] = 0
        for i in range(n-1, -1, -1):
            if temp:
                lst[i][c] = temp.pop()

# 한 뭉탱이가 몇개의 숫자로 이루어 졌는지 세는 함수
def dfs(x, y):
    visited[x][y] = True 
    
    cnt = 1   
    for i  in range(4):
        nx, ny = x+dxs[i], y+dys[i]
        # if in_range(nx,ny) and visited[nx][ny] == False and lst[x][y] == lst[nx][ny]:
        #     cnt += dfs(nx, ny)
        # else:continue
        if not in_range(nx,ny):continue
        if visited[nx][ny] == True or lst[x][y] != lst[nx][ny] : continue
        cnt += dfs(nx, ny)
    return cnt 

# K개 이상이라면 호출하고 뭉탱이를 0으로 바꿔주는 함수
def dfs_del(x,y, v):
    visited2[x][y] = True # 지워줬다는 거 표시하고 
    lst[x][y] = 0 # 지움
    
    for i in range(4):
        nx, ny = x+dxs[i], y+dys[i]
        if in_range(nx, ny) and visited2[nx][ny] == False and lst[nx][ny]==v:
            dfs_del(nx, ny, v)
        else:continue

while 1:
    exist = False
    
    # 여기서 계속 초기화 해줘야 하는 이유를 정확히 모르겟다...

    visited = [[False]*10 for _ in range(n)] # 뭉탱이 개수 셀때 
    visited2 = [[False]*10 for _ in range(n)] # 뭉탱이 지워줄 때
    for i in range(n):
        for j in range(10):
            if lst[i][j] != 0:
                cnt = dfs(i,j)
            if cnt >= k:
                dfs_del(i, j, lst[i][j])
                exist = True
    if not exist:
        break
    else:
        gravity(lst)

for i in lst:
    for j in i:
        print(j, end="")
            
            
    
    