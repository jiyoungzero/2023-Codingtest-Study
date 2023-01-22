# 2023.01.14. 재풀이
# 브론즈 2
N, M = map(int, input().split())
card = list(map(int, input().split()))

result = 0

for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp = card[i] + card[j] + card[k]
            if temp <= M:
                result = max(result, temp)
'''
# 배열, 완전탐색, 난이도 하 , 20분
# 3중 for문 사용
# 답안과 거의 동일하게 풀이함
# max함수를 쓰기 위해선 변수 다르게 해야함

num, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))

result = 0

for i in range(0, num):
    for j in range(i+1, num):
        for k in range(j+1, num):
            temp = arr[i] + arr[j] + arr[k]
            if temp <= m:
                result = max(result, temp)

print(result)
'''
