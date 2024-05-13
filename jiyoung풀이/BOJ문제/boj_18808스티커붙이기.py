import sys
input = sys.stdin.readline


# row값이 작을 수록, col값이 작을 수록
def rotate_90(arr):
    n = len(arr)
    m = len(arr[0])
    
    r_arr = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            r_arr[j][n-i-1] = arr[i][j]
    return r_arr

def find(st):
    row, col = len(st), len(st[0])
    possible = []
    for i in range(n-row+1):
        for j in range(m-col+1):
            flag = True
            # print(st, i, j, i+row, j+col)
            for x in range(i, i+row):
                for y in range(j, j+col):
                    # print(st, x, y, i+row, j+col)
                    if board[x][y] == 1 and st[x-i][y-j] == 1:
                        # print("불가", x, y, x-i, y-j)
                        flag = False
                        break
            if flag:
                possible.append([i, j, i+row, j+col])
    possible.sort(key = lambda x:(x[0], x[1]))
    return possible 
                
def put_sticker(places, st):
    global board
    place = places[0]
    sr, sc, er, ec = place
    for i in range(sr, er):
        for j in range(sc, ec):
            if st[i-sr][j-sc] == 1:
                board[i][j] = 1
            

def simulate(sticker):
    times = 0
    while times < 4:
        times += 1
        places = find(sticker)
        # print("ddddddd -->", places)
        if len(places) > 0:
            put_sticker(places, sticker)
            break
        else:
            sticker = rotate_90(sticker)
        


n, m, k = map(int ,input().split())
board = [[0]*m for _ in range(n)]
stickers = []

for _ in range(k):
    ri, _ = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(ri)]
    simulate(sticker)
    
# print("--------")
answer = 0
for row in board:
    answer += row.count(1)
print(answer)
    
    
    
    
    