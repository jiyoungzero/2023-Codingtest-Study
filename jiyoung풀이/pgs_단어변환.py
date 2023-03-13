# dfs/bfs
def solution(begin, target, words):
    if target not in words: return 0
    answer = 0
    list_begin = list(begin)
    list_target = list(target)
    n = len(list_begin)
    new_words = [[] for i in range(len(words))]
    
    for i, a in enumerate(words):
        for j, b in enumerate(words):
            if len(set(list(a)) & set(list(b))) == n-1:
                new_words[i].append(b)
    print(new_words)
                
    
    
    return answer