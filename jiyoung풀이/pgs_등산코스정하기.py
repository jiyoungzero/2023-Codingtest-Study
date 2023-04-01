# 2022 카카오 tech 인턴십

# 첫풀이 -> 실패 (summit반영 안함)
import heapq

def solution(n, paths, gates, summits):
    answer = []
    leaves = [ [] for _ in range(n+1)]
    intensity = [int(1e9)] * (n+1)    
    for path in paths:
        start, end, cost = path
        leaves[start].append((end, cost))
        leaves[end].append((start, cost))
    print(leaves)
    
    searchIntensity(summits[0],intensity,leaves)
    for i in range(1, n+1):
        if intensity[i] == int(1e9):print("not pass")
        else:print(intensity[i])
        
    return answer

def searchIntensity(start,intensity,leaves):
    q = []
    heapq.heappush(q, (0, start))
    intensity[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if intensity[now] < dist: continue
        for leaf in leaves[now]:
            cost = dist + leaf[1]
            if cost < intensity[leaf[0]]:
                intensity[leaf[0]] = cost
                heapq.heappush(q, (cost, leaf[0]))