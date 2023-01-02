# 구현 

# r = (0, 1) u = (-1, 0) d = (1, 0) l = (0, -1)
# 리스트 한 줄에 한번에 출력하기 

# 모범답안 

n =int(input())
x,y =1,1
plans = input().split()

dx,dy = [0, 0, -1, 1],[-1,1,0,0]
move_types= ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue
            x, y = nx, ny
print(x, y)
            

