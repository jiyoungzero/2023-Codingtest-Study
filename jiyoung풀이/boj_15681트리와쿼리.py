# 이진트리


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(parent):
    count[parent] = 1
    for child in graph[parent]:
        if not count[child]:
            dfs(child)
            count[parent] += count[child]


n, r, q = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queries = [int(input()) for _ in range(q)]
count = [0]*(n+1)

dfs(r) 

for query in queries:
    print(count[query])


        



