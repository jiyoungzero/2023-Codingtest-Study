import sys
input = sys.stdin.readline 
from collections import defaultdict

n = int(input())
like_info = dict()
arr = [[0]*n for _ in range(n)]
for i in range(n*n):
    idx, a, b, c, d = list(map(int, input().split()))
    like_info[idx] = [a, b, c, d]
taken = [[False]*n for _ in range(n)]

answer = 0
dxs, dys = [0,0,-1,1], [1,-1,0,0]


def satisfied_num():
    global answer, arr
    for i in range(n):
        for j in range(n):
            tmp = 0
            target = arr[i][j]
            for k in range(4):
                ni, nj = i +dxs[k], j+dys[k]
                if not in_range(ni, nj):continue
                if arr[ni][nj] in like_info[target]:
                    tmp += 1
            if tmp == 1:answer += 1
            elif tmp == 2: answer += 10
            elif tmp == 3 : answer += 100
            elif tmp == 4: answer += 1000 
            else: continue
            
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def seat(target):
    global taken, like_info
    
    # [좋아하는 학생 수, 빈 자리 수, 행번호, 열번호]
    # sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    possible = []
    for i in range(n):
        for j in range(n):
            if taken[i][j]:continue
            space = 0 # 빈자리
            like = 0 # 좋아하는 학생 수
            for k in range(4):
                ni, nj = i + dxs[k], j + dys[k]
                if not in_range(ni, nj):
                    continue
                if not taken[ni][nj]:space+=1
                if arr[ni][nj] in like_info[target]:
                    # print("like = ", like_info[arr[ni][nj]])
                    like += 1
            possible.append((like, space, i, j))
    possible.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    return (possible[0][2], possible[0][3])
            
for i in like_info.keys():
    print(i)
    x, y = seat(i)
    taken[x][y] = True
    arr[x][y] = i


satisfied_num()
print(answer)
                
                
            