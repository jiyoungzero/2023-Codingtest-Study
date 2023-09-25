n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = -1e9
max_value = 1e9

def dfs(depth, now):
    global min_value, max_value, add, sub, mul, div
    if depth == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
        return 
    
    else:
        if add > 0:
            add -= 1
            dfs(depth+1, now+data[depth])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(depth+1, now-data[depth])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(depth+1, now * data[depth])
            mul += 1
        if div > 0:
            div -= 1
            dfs(depth+1, int(now/data[depth]))
            div += 1
    
dfs(1, data[0])
print(min_value, max_value)
            