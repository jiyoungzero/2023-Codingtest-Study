# 문제 스스로 풀어보기

# 보너스 점수를 줄 변수, 각 (리스트 인덱스 +1 )한 점수를 더하면 될 듯

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(str, input()))
bonus, result = 0,0
flag = False # 문제 틀리면 True로 전환해서 보너스 점수 초기화
# 19~
for i in range(len(lst)):
    if lst[i] == 'O':
        result += (i+1) + bonus
        flag = False
        bonus += 1
    else:
        flag = True
        bonus = 0
print(result)
