# 2018 카카오 블라인드

# 75점 -> 왜??
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return 5*len(cities)
    
    for c in cities:
        if c.lower() not in cache:
            if len(cache) < cacheSize:
                cache.append(c.lower())
            else:
                cache.popleft()
                cache.append(c.lower())
            answer += 5
        else:
            answer += 1

    return answer