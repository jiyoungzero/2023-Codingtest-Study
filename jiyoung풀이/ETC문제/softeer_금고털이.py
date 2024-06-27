import sys
input = sys.stdin.readline 

w, n = map(int, input().split())
jewerlys = [tuple(map(int, input().split())) for _ in range(n)] # 금속의 무게, 무게 당 가치 
answer = 0


jewerlys.sort(key = lambda x:(-x[1]))
left_w = w
for j in jewerlys:
    if left_w >= j[0]:
        answer += (j[0]*j[1])
        left_w -= j[0]
    else:
        answer += (left_w*j[1])
        break
print(answer)