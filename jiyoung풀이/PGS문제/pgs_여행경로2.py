# DFS 풀이

from collections import defaultdict
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    tickets.sort(reverse = True)
    for s, e in tickets:
        graph[s].append(e)

    
    print(graph)
    path = ['ICN']
    while path:
        now = path[-1]

        
        if graph[now]: 
            path.append(graph[now].pop())
        else:
            answer.append(path.pop())
            
        
    print(answer)
    return answer[::-1]


# BFS 풀이
from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN",["ICN"], []))
    
    while q:
        airport, path, used = q.popleft()

        if len(used) == len(tickets):
            answer.append(path)
        
        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used:
                q.append((ticket[1], path+[ticket[1]], used+[idx]))
                
    
    answer.sort()

    return answer[0]