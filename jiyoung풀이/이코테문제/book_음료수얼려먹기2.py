import sys
input = sys.stdin.readline

row, col = map(int, input().split())
arr = []
visited = [[False]*col for _ in range(row)]
result = 0

for i in range(row):
    arr.append(list(map(int, input().rstrip())))
    
def dfs(r, c):
    if r < 0 or r >= row or c < 0 or c >= col:
        return False
    if not visited[r][c] and arr[r][c] == 0:
        visited[r][c] = True
        
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
        return True
    return False

        
for i in range(row):
    for j in range(col):
        if dfs(i, j):
            result += 1

print(result)