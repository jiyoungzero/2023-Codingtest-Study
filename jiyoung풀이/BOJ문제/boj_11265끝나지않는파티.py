import sys
input = sys.stdin.readline 

n, m = map(int ,input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
requests = []
for _ in range(m):
    requests.append(list(map(int, input().split())))
    
distance = [[int(1e9)]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        distance[i][j] = matrix[i][j]
    
for k in range(n):
    for a in range(n):
        for b in range(n):
            distance[a][b] = min(distance[a][b], distance[a][k]+distance[k][b])


for req in requests:
    a, b, c= req
    if distance[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")    
