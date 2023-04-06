# 디버깅 -> 오답 이유 찾기
import sys
input = sys.stdin.readline
# 오른쪽 : 1, 왼쪽 : 2, 위쪽 : 3, 아래쪽 : 4
n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

dice = [0,0,0,0,0,0]

# [1,2,3,4,5,6]  -> 현재 바닥 : 6, 현재 위: 1
# command == 4 / 아래쪽으로 굴렸을 때,
# [5,1,3,4,6,2]

# command == 3 / 위쪽으로 굴렸을 때, 
# [2,6,3,4,1,5]

# command == 2 / 왼쪽으로 굴렸을 때,
# [3,2,6,1,5,4]

# command == 1 / 오른쪽으로 굴렸을 때, 
# [4,2,1,6,5,3]

nx, ny = x, y
prev = [0, 0]
# 바닥 dice[-1], 위 dice[0]
for c in command:
    if n <= nx or nx < 0 or m <= ny or ny < 0:
        nx -= prev[0]
        ny -= prev[1]
        continue
    if c == 4:
        dice = [dice[4],dice[0], dice[2], dice[3], dice[-1], dice[1]]
        if arr[nx][ny] != 0:
            dice[-1] = arr[nx][ny]
            arr[nx][ny] = 0
        else:
            arr[nx][ny] = dice[-1]
        print(dice[0])
        
        #위치 업데이트
        nx += 1
        prev = [1, 0]

    elif c == 3:
        dice = [dice[1],dice[-1], dice[2], dice[3], dice[0], dice[4]]
        if arr[nx][ny] != 0:
            dice[-1] = arr[nx][ny]
            arr[nx][ny] = 0
        else:
            arr[nx][ny] = dice[-1]
        print(dice[0])
        
        #위치 업데이트
        nx -= 1 
        prev = [-1, 0]       
        
    elif c == 2:
        dice = [dice[2],dice[1], dice[-1], dice[0], dice[4], dice[3]]
        if arr[nx][ny] != 0:
            dice[-1] = arr[nx][ny]
            arr[nx][ny] = 0
        else:
            arr[nx][ny] = dice[-1]
        print(dice[0])
                
        #위치 업데이트
        ny -= 1
        prev = [0, -1]
    else:
        dice = [dice[3],dice[1], dice[0], dice[-1], dice[4], dice[2]]
        if arr[nx][ny] != 0:
            dice[-1] = arr[nx][ny]
            arr[nx][ny] = 0
        else:
            arr[nx][ny] = dice[-1]
        print(dice[0])
                
        #위치 업데이트
        ny += 1
        prev = [0, 1]
        



