import sys
from collections import Counter
input = sys.stdin.readline


n, m = map(int, input().split())
lst = list(map(int, input().split()))
cnt = Counter(lst)
lst_cnt = []
result = 0
for ele in cnt:
    lst_cnt.append([ele, cnt[ele]])


for i in range(len(lst_cnt)):
    target = lst_cnt[i][1]
    mul = 0
    for j in range(i+1, len(lst_cnt)):
        mul += lst_cnt[j][1]
    result += (target*mul)
print(result)

    
    