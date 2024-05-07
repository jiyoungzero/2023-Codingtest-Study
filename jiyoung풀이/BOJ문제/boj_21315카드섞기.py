import sys
input = sys.stdin.readline

n = int(input())
result = map(int, input().split())
answer = []


def simulate(sel):
    # 초기상태
    cards = [i for i in range(1, n+1)]
    for num in sel:
        before= cards[1:]
        cards = cards[1:] + cards[0]
        for i in range(2, num):
            ups = before[-2**(num-i+1):]
            cards = ups + ups[:2**(num-i+1)] + cards[0]
            before = ups
    for a, b in zip(result, cards):
        if a != b:
            return False
    return True


def select_2num(sel, idx):
    global answer
    if len(sel) == 2:
        if simulate(sel):
            answer = sel
            return 
        
    if idx == n+1:
        return 
    
    for i in range(1, n+1):
        if i not in sel:
            select_2num(sel+[i], idx+1)


select_2num([], 1)
print(*answer)

            
        