#문제 스스로 풀어보기

import sys
input = sys.stdin.readline

# 중간값 인덱스 n // 2 + 1

n = int(input())
lst = list(map(int, input().split()))

lst.sort() # 내림차순 정렬

m_idx = ((n-1) // 2) 
print(lst[m_idx])