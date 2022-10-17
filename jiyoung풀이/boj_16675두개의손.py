# 문제 스스로 풀어보기

import sys
input = sys.stdin.readline

ml,mr, tl, tr = map(str, input().split())

# "s" > "p"
# "p" > "r"
# "r" > "s"
win = [["S", "P"], ["P", "R"], ["R","S"]]

if ([ml, tl] in win and [ml, tr] in win) or ([mr, tl] in win and [mr, tr] in win) :
        print("MS")
elif ([tl, ml] in win and [tl, mr] in win) or ([tr, ml] in win and [tr, mr] in win):
        print("TK")
else:
    print("?")