blocks = [[[1, 1, 1, 1]], [[1, 1], [1, 1]],
        [[1, 0], [1, 0], [1, 1]], 
        [[1, 0],[1, 1], [0, 1]],
        [[1, 1, 1], [0, 1, 0]]]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def rotate_90(grid):
    # rotated_grid = [[0]*n for _ in range(m)]
    # for i in range(n):
    #     for j in range(m):
    #         rotated_grid[j][max(n-i-1, 0)] = grid[i][j]
    rotated = list(zip(*grid[::-1]))
    return [list(row) for row in rotated]

def up_down_reverse(grid):
    reversed_grid = grid[::-1]
    return reversed_grid

def right_left_reverse(grid):
    reversed_grid = []
    for row in grid:
        reversed_grid.append(row[::-1])
    return reversed_grid

def block_in_range(x, y, block):
    h, w = len(block), len(block[0])
    return 0 <= y+w-1 < m and 0 <= x + h -1 < n 

def get_sum(block):
    global arr
    h, w= len(block), len(block[0])
    result = 0
    
    for i in range(n):
        for j in range(m):
            tmp = 0
            if block_in_range(i, j, block):
                # 블록 내의 숫자 합하기
                for x in range(h):
                    for y in range(w):
                        if block[x][y]:
                            tmp += arr[i+x][j+y]
            result = max(result, tmp)
    return result

for block in blocks:
    # 회전만 시키기
    for _ in range(4):
        answer = max(answer, get_sum(block))
        # print(get_sum(block))
        block = rotate_90(block)
        
    # 상하 대칭 후 회전
    block = up_down_reverse(block)
    for _ in range(4):
        answer = max(answer, get_sum(block))
        block = rotate_90(block)
    block = up_down_reverse(block) # 원상복귀
    
    
    # 좌우 대칭 후 회전 
    block = right_left_reverse(block)
    for _ in range(4):
        answer = max(answer, get_sum(block))
        block = rotate_90(block)
    block = right_left_reverse(block) # 원상복귀

print(answer)