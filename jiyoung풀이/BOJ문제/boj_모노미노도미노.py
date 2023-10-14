import sys
input =sys.stdin.readline

n = int(input())
command = [list(map(int, input().split())) for _ in range(n)]

# t = 1 :1*1 (x, y)
# t = 2 :1*2 (x, y), (x, y+1)
# t = 3 :2*1 (x, y), (x+1, y)

red_arr = [[0]*4 for _ in range(4)]
blue_arr = [[0]*6 for _ in range(4)]
green_arr = [[0]*4 for _ in range(6)]

def rotate(array): # 반시계 방향으로 90도 회전 
    n = len(array)
    m = len(array[0])
    r_arr = [[0]*n for _ in range(m)]
    for j in range(m):
        for i in range(n):
            r_arr[j][i] = array[i][m-1-j]
    return r_arr


# 타일 위치시키기
def locate_blue(t, a, b):
    if t == 1: 
        for j in range(5, -1, -1):
            if blue_arr[a][j] == 0:
                blue_arr[a][j] = 1 # 블록 : 1
                break
    elif t == 2:
        for j in range(5, -1, -1):
            if blue_arr[a][j] == 0:
                blue_arr[a][j-1] = 1
                blue_arr[a][j] = 1
                break
    elif t == 3:
        for j in range(5, -1, -1):
            if blue_arr[a][j] == 0 and blue_arr[a+1][j] == 0: 
                blue_arr[a][j] = 1
                blue_arr[a+1][j] = 1
                break

def locate_green(t, a, b):
    if t == 1:
        for i in range(5, -1, -1):
            if green_arr[i][b] == 0:
                green_arr[i][b] = 1 # 블록 : 1
                break
    elif t == 2:
        for i in range(5, -1, -1):
            if green_arr[i][b] == 0 and green_arr[i][b+1] == 0:
                green_arr[i][b] = 1
                green_arr[i][b+1] = 1
                break
    elif t == 3:
        for i in range(4, -1, -1):
            if green_arr[i+1][b] == 0:
                green_arr[i+1][b] = 1
                green_arr[i][b] = 1
                break
def b_shift(idx): # idx: 지워진 열 
    # 1. blue배열 반시계 방향으로 
    # 2. 비워진 열 아래부분을 한칸씩 위로 올리기
    # 3. rotate 3번해줘서 원상복귀시키기

    # 5번째 row가 비워진 경우 
    if idx == 5:
        return 
    
    rotate(blue_arr)
    # 0~4번째 row가 비워진 경우
    for r in range(idx+1, 6):
        for c in range(4):
            blue_arr[r-1][c] = blue_arr[r][c]
    for c in range(4):
        blue_arr[5][c] = 0
    
    for _ in range(3):
        rotate(blue_arr)

def g_shift(idx):  
    # 0번째 row가 비워진 경우 
    if idx == 0:
        return 
    
    # 1~5번째 row가 비워진 경우
    # 위의 행을 아래행으로 내리기
    for r in range(idx-1, -1, -1):
        for c in range(4):
            green_arr[r+1][c] = green_arr[r][c]
    for c in range(4):
        green_arr[0][c] = 0       


# 타일 없애고,없앤 줄 이동시키고, 점수 얻기
def blue_point():
    b_result = 0
    for j in range(6):
        n_blue_arr = rotate(blue_arr)
        if sum(n_blue_arr[j]) == 4:
            # 타일 없애기
            for i in range(4):
                blue_arr[i][j] = 0
            # 한줄씩 오른쪽으로 보내기
            b_shift(j)
            # 점수 얻기
            b_result += 1
    return b_result

def green_point():
    g_result = 0 
    for i in range(6):
        if sum(green_arr[i]) == 4:
            # 타일 없애기
            for j in range(4):
                print("green없앴나요..", (i,j))
                green_arr[i][j] = 0
            # 한줄씩 내리기
            g_shift(i)
            
            # 점수 얻기
            g_result += 1
    return g_result       
        

# 타일 개수 세기    
def count_tile(): 
    # blue
    cnt = 0
    for i in range(4):
        for j in range(6):
            if blue_arr[i][j] == 1:
                cnt += 1
    for i in range(6):
        for j in range(4):
            if green_arr[i][j] == 1:
                cnt += 1
    return cnt 
                


b_p, g_p = 0, 0
for c in command:
    t, x, y = c
    
    locate_blue(t, x, y)
    locate_green(t, x, y)
    
    b_p += blue_point()
    g_p += green_point()


# 확인 
for i in range(6):
    print(green_arr[i])
for j in range(4):
    print(blue_arr[j])

print(b_p+g_p)
print(count_tile())
        







