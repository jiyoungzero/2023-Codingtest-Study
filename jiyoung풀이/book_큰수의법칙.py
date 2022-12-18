# greedy 문제 

# 문제 : 큰수의 법칙 문제. 주어진 수들을 m번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다. 

# input : 5 8 3 \n 2 4 5 4 6 , output : 46

import sys
input = sys.stdin.readline

n, m , k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

arr.sort(reverse=True)
cnt = 0
first = arr[0]
second = arr[1]

# while True:
#     if first != second:
#         if cnt == m : break
#         for _ in range(k):
#             if cnt == m: break
#             result += first 
#             cnt += 1
#         if cnt != m:
#             result += second
#             cnt += 1
            
#     if first == second:
#         for _ in range(m):
#             result += first

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:break
    result += second
    m -= 1
    
print(result)

## 시간초과 해결 ㅇ
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)