import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [-1]*(n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def dfs(start):
    for i in tree[start]:
        if parent[i] == -1:
            parent[i] = n
            dfs(i)

dfs(1)
for i in range(2, n+1):
    print(parent[i])