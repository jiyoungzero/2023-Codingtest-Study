# 문제 스스로 풀어보기 
import sys
input = sys.stdin.readline

# 3*3 행렬을 검사하는데, 다른 부분이 있으면 +1 
n, m = map(int, input().split())
arr_A = [list(map(int,input().rstrip())) for _ in range(n)]
arr_B = [list(map(int,input().rstrip())) for _ in range(n)]
ans = 0

def flip(i, j):
    for a in range(i,i+3):
        for b in range(j, j+3):
            # if arr_A[a][b] != arr_B[a][b]: 그냥 다 뒤집기
                arr_A[a][b] = 1 - arr_A[a][b] 

# if n<3 or m<3: ans = -1 --> 이거 땜에 계속 틀렸음 왜??
for i in range(n-2):
    for j in range(m-2):
        # 3*3 뒤집기 최소
        if arr_A[i][j] != arr_B[i][j]:
            flip(i,j)
            ans+=1

# 다 연산 끝내고
if arr_A != arr_B:ans = -1
if ans == -1:
    print("-1")
else:
    print(ans)
                
            
    
    