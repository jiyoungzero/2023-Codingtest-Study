# 2018 카카오 블라인드

# 75점 -> 왜?? cacheHit 됏을때는 옛날의 버젼을 지우고 최신 버젼으로 업데이트 해주어야 LRU방식이 유지될 수 있다.!

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
            cache.remove(c.lower())
            answer += 1
            cache.append(c.lower())

    return answer


# 다른 풀이 maxlen 중요 굿~
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
