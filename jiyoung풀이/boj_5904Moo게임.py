# 분할정복 -> 이게 어딜 봐서 분할정복인지..?
import sys
input = sys.stdin.readline

# Moo(n) = Moo(n-1) + "m" + "o"*(n+2) + Moo(n-1)
# Moo(n)는 +를 기준으로 분할정복을 할 수 있음
# len(Moo(n-1)) = Moo(n)의 가운데 부분 빼고 // 2
# 각 부분에서 N이 존재하면 그게 답 

N = int(input())

