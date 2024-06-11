from collections import defaultdict
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for s, e in tickets:
        graph[s].append(e)
        
    print(graph)
    return answer