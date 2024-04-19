import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)

parent = [[] for _ in range(n+1)]

def dfs(node):
    global parent
    if not graph[node]:
        return 
    
    for leaf in graph[node]:
        if parent[leaf] == []:
            parent[leaf] = node 
            dfs(leaf)
dfs(1)
# print(graph)
for ele in parent[2:]:
    print(ele)
    


