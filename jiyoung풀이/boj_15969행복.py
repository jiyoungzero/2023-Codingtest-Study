# 문제 스스로 풀어보기 

# 문제 파악 : 

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

max_value = max(lst)
min_value = min(lst)
print(max_value-min_value)