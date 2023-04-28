# 
def solution(wallpaper):
    answer = []
    start_x, start_x, end_x, end_y = 0,0,0,0 # 모든 #의 위치 중 가장 작은 y값, 가장 작은 x값, 가장 큰 y값, 가장 큰 x값
    r, c = len(wallpaper), len(wallpaper[0])
    x_lst,y_lst = [], []
    for i in range(r):
        for j in range(c):
            if wallpaper[i][j] == "#":
                x_lst.append(i+1)
                y_lst.append(j+1)
    print(x_lst, y_lst)

    start_x, start_y = min(x_lst), min(y_lst)
    end_x, end_y = max(x_lst), max(y_lst)
    return [ start_x-1, start_y-1, end_x, end_y]