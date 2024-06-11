from collections import defaultdict, deque
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    tickets.sort()
    
    for s, e in tickets:
        graph[s].append(e)
        
    print(graph)
    que = deque()
    que.append('ICN')
    while que:
        now = que.popleft()
        answer.append(now)
        
        if graph[now]:
            que.append(graph[now][0])
            graph[now] = graph[now][1:]
    return answer