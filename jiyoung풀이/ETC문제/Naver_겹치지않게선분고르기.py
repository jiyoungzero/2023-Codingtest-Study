n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0
selected = []

def overlap(seg1, seg2):
    a, b = seg1
    c, d = seg2
    return (c <= a and a <= d) or (c <= b and b <= d) or (a<= c and c<= b) or (a<= d and d <= b)

def possible():
    for i, seg1 in enumerate(selected):
        for j, seg2 in enumerate(selected):
            if i != j and overlap(seg1, seg2):
                return False
    return True

def solution(cnt):
    global answer
    if cnt == len(lines):
        if possible():
            answer = max(answer, len(selected))
        return 
    
    selected.append(lines[cnt])
    solution(cnt + 1)
    selected.pop()

    
    solution(cnt + 1)

            
solution(0)
print(answer)