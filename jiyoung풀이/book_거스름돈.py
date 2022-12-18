# greedy 알고리즘의 가장 대표적인 문제 

# 문제 : 가운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 짜리 동전이 무한히 존재한다고 가정한다. 
# 손님에게 거슬러 줘야 할 돈이 n원일때, 거슬러줘야 할 동전의 최소 개수를 구하라.
# 단 거슬러 줘야 할 돈 n은 항상 10의 배수이다. 

# input : 1260 --> output : 6개
import sys
input = sys.stdin.readline

n = int(input())

coin = [500, 100, 50, 10]
result = 0

for c in coin:
    result += n // c
    n %= c
print(result)    


