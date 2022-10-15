# 브론즈 2

n = int(input())
s = list(input().strip())
score = 0
bonus = 0

for i in range(n):
    if s[i] == 'O':
        score += (i+1) + bonus
        bonus += 1
    elif s[i] == 'X':
        bonus = 0

print(score)
