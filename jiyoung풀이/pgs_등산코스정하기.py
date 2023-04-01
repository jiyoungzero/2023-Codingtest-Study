# 2022 카카오 tech 인턴십

# 첫풀이 -> 실패 
import heapq

def solution(n, paths, gates, summits):
    leaves = [ [] for _ in range(n+1)]
    intensity = [int(1e9)] * (n+1)    
    for path in paths:
        start, end, cost = path
        leaves[start].append((end, cost))
        leaves[end].append((start, cost))

    answer = searchIntensity(gates,summits,intensity,leaves)   
    return answer

def searchIntensity(gates, summits,intensity,leaves):
    q = []
    for gate in gates:
        heapq.heappush(q, (0, gate))
        intensity[gate] = 0
        
    while q:
        dist, now = heapq.heappop(q)
        if now in summits or intensity[now] < dist: continue 
        for leaf in leaves[now]:
            next_dist = max(dist,leaf[1]) 
            if next_dist < intensity[leaf[0]]:
                intensity[leaf[0]] = next_dist
                heapq.heappush(q, (next_dist, leaf[0]))
                
    result = [0, int(1e9)]
    for summit in summits:
        if intensity[summit] < result[1]:
            result[1] = intensity[summit]
            result[0] = summit
    return result
        