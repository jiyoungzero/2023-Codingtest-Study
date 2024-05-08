import sys
from itertools import permutations
input = sys.stdin.readline 

n = int(input())
result = list(map(int, input().split()))
answer = []

def shuffle(card1, card2, card3):
    card = card2 + card1 + card3
    if len(card2) > 1:
        return shuffle(card2[:len(card2)//2] + card1, card2[len(card2)//2:], card3)
    else:
        return card

flag = False
def select_2nums(idx, sel):
    global answer, flag
    if len(sel) == 2:
        cards = [i for i in range(1, n+1)]
        for k in sel:
            card1 = []
            card2 = cards[n-(2**k):] # 위로 보낼
            card3 = cards[:n-(2**k)] # 아래
            cards = shuffle(card1, card2, card3)
        # print(sel, cards)
        if result == cards:
            answer = sel
            flag = True
            return 
    if flag:
        return
    
    if idx == n+1:
        return 
    
    for i in range(1, n+1):
        if i not in sel:
            select_2nums(idx+1, sel + [i])

select_2nums(0, [])
print(*answer)