import sys
from collections import Counter
input = sys.stdin.readline


n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0
arr = [0]*11 # 1~10까지의 무게를 담는 리스트

for ele in data:
    arr[ele] += 1

for i in range(1, m+1):
    n -= arr[i]
    result += (arr[i]*n)

print(result)



    
    