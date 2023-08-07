# 구현

import sys
input = sys.stdin.readline

n = int(input())

lst_n = list(str(n))
left, right = 0,0

for i in range(len(lst_n)//2):
    left += int(lst_n[i])
for j in range(len(lst_n)//2, len(lst_n)):
    right += int(lst_n[j])

if left == right:
    print("LUCKY")
else:
    print("READY")



