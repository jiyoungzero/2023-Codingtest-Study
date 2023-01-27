# 분할정복, 재귀
import sys
input = sys.stdin.readline
# 1. 구역이 모두 같은 색이 아니라면 -> n/2, n/2 -> 4 덩어리로 나누기
# >> 8 -> 4 -> 2 -> 1, paper(시작점, 종이크기)
# 2. 모두 같은 색이거나 하나의 칸일 때까지 1번 반복
# 3. 파란색 : 1, 하얀색 : 0 -> 덩어리의 개수 세기

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
w_cnt, b_cnt = 0,0


def paper(row, col, n): 
    global w_cnt, b_cnt
    
    # while n != 1:# 한칸이면 탈출
    for i in range(row, row+n):
        for j in range(col, col+n):
            if arr[row][col] != arr[i][j]: # 다르면 나누기
                paper(row, col, n//2)
                paper(row, col+n//2, n//2)
                paper(row+n//2,col, n//2)
                paper(row+n//2, col+n//2, n//2)
                return
    if arr[row][col] == 1:
        b_cnt += 1
    else:
        w_cnt += 1
    
    
paper(0,0,n)
print(w_cnt, b_cnt)
