from collections import deque
import sys
input =sys.stdin.readline

# 모든 간선의 비용이 동일(여기서는 1로 동일)할 때는 bfs 너비 우선탐색이 유용

n, m , k , x = map(int, input().split()) # 도시의 개수, 도로의 개수, 거리정보, 출발 도시
lst = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    
distance = [-1] * (n+1)
distance[x] = 0

que = deque()
que.append([x])

while que:
    now = que.popleft()
    for next in lst[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            que.append(next)

# 최단 거리가 k인 도시를 오름차순으로 정렬
flag = False
for i, ele in enumerate(distance):
    if ele == k :
        print(i)
        flag = True
        
if flag == False:
    print(-1) 

    
