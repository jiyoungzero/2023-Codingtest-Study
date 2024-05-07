import sys
input = sys.stdin.readline

n = int(input())
result = map(int, input().split())
answer = []
# 초기상태
cards = [i for i in range(1, n+1)]

def simulate(sel):
    pass


def select_2num(sel, idx):
    global answer
    if len(sel) == 2:
        print(sel)
        if simulate(sel):
            answer = sel
            return 
        
    if idx == n+1:
        return 
    

    select_2num(sel+[idx], idx+1)
    
    select_2num(sel, idx+1)

select_2num([], 1)

            
        