def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    arr = [[-1]*51 for _ in range(51)]
    for rec in rectangle:
        sc, sr, ec, er = rec
        for i in range(sr, er+1):
            for j in range(sc, ec+1):
                if arr[i][j] == 0:continue
                if i == sr or i == er or j == sc or j == ec:
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0
    for row in arr:
        print(*row[:11])
                    
    return answer