# dfs, bfs

from collections import deque

def bfs(graph, start, visited):
    que = deque()
    ans = []
    que.append(start)
    visited[start] = True
    ans.append(start)
    while que:
        cur = que.popleft()
        for leaves in cur:
            if not visited[leaves]:
                que.append(leaves)
                visited[leaves] = True
                ans.append(leaves)
    return ans
    

def solution(tickets):
    answer = []
    tickets.sort(key=lambda x:x[1])
    airport = dict()
    tmp = 0
    for t in tickets:
        for ele in t:
            if ele not in airport:
                tmp += 1
                airport[ele] = tmp
    print((airport))
    route = [[] for i in range(len(airport)+1)]
    visited = [False] * (len(airport)+1)  
    
    
    for t in tickets:
        start, end = t[0], t[1]
        route[airport[start]].append(airport[end])
    
    print(route)
    que = deque()
    ans = []
    que.append(airport["ICN"])
    # visited[airport["ICN"]] = True
    ans.append(airport["ICN"])
#     while que:
#         cur = que.popleft()
#         for leaves in route[cur]:
#             # if not visited[leaves]:
#             que.append(leaves)
#                 # visited[leaves] = True
#             ans.append(leaves)
        
#     print(ans)
#     convert_airport = {v:k for k,v in airport.items()} 
#     for r in ans:
#         answer.append(convert_airport[r])
    
        
    return answer