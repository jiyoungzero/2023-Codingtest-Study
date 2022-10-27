# 실버1
# DP
# 5시 10분 시작
# Top-Down
# 바로 밑이랑 바로 밑 오른쪽으로만 갈 수 있음

#  1. [i][0] : [i-1][0] 항목을 그대로 더함  
#  2. [i][i] : [i-1][i] 항목을 그대로 더함  
#  3. 나머지 : max([i-1][j-1],[i-1][j]) 더함.

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0 :
            arr[i][0] += arr[i-1][0]              
        elif j == i :
            arr[i][j] += arr[i-1][j-1] 
        else :
            arr[i][j] += max(arr[i-1][j-1],arr[i-1][j]) # 큰 것만

print(max(arr[-1]))