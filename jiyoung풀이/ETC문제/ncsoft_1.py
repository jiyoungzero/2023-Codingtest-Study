import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
# n : 도시 개수
# k : 수도여야 하는 도시의 최소 비용
# edges -> [a, b, c] : a-b사이의 도시 비용은 c

    
def solution(n, k, capitals, edges):
    answer = []
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start)) 
        distance[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
        
    # 모든 경우에...
    for i in range(1,n+1):
        distance = [INF]*(n+1)
        graph = [[] for i in range(n+1)]
    
        for e in edges:
            a, b, c = e[0], e[1], e[2]
            graph[a].append((b,c))
            graph[b].append((a,c))
            
        dijkstra(i)
        for cap in capitals:
            if distance[cap] <= k:
                answer.append(i)
                break
            
    for ele in answer:
        if ele > 0 and not in capitals:
            result.append(ele)
            
    return answer
