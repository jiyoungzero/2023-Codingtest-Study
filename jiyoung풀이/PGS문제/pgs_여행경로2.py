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