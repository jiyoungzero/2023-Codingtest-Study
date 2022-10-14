# 브론즈1
# 20분

from re import L


n, l, k = map(int, input().split())

if (n < 1 and n > 100) or (k < 0 and k > n) or (l < 1 and l > 50):
    n, l, k = map(int, input().split())

score = 0

exam = []
for i in range(n):
    exam.append([])
    a, b = map(int,  input().split())

    exam[i].append(a)
    exam[i].append(b)
exam.sort(key=lambda x: (x[1], x[0]), reverse=True)

cnt = 0
for i in range(n):
    if cnt < k:
        if exam[i][1] <= l:
            score += 140
        elif exam[i][0] <= l:
            score += 100
    else:
        break
print(score)
