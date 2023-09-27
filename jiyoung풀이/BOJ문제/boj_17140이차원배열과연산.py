import sys
input = sys.stdin.readline
from collections import Counter 

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
time = 0
r, c = r-1, c-1

def R(a):
    tmp = []
    max_len = 0
    for i in a:
        row = []
        target = (Counter(i))
        target = list(target.items())
        max_len = max(max_len, len(target)*2)
        
        target.sort(key=lambda x:(x[1], x[0]))
        
        for i in range(len(target)):
            if i > 50 :break
            else:
                v, k = target[i]
                if v == 0:break
                row.append(v)
                row.append(k)
        tmp.append(row)
    
    # 나머지 부분은 0으로 채우기
    for i in range(len(a)):
        if len(tmp[i]) <= max_len:
            for _ in range(max_len-len(tmp[i])):
                tmp[i].append(0)
    return tmp
    
    
    

def solution():
    global arr, time
    while True:
        if arr[r][c] == k or time >= 100:
            break
        
        if len(arr) >= len(arr[0]):
            arr = R(arr)
        else:
            arr = list(map(list, zip(*arr)))
            arr = R(arr)
            arr = list(map(list, zip(*arr)))
        time += 1
    return time if time < 100 else -1

print(solution())
print(R(arr))