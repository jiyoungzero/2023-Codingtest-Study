# 브론즈1
# 20분
# hard 태스크를 최대한 많이 풀어야함

n, l, k = map(int, input().split())
score = 0
hard, easy = 0, 0
cnt = 0
for i in range(n):
    sub1, sub2 = map(int,  input().split())
    if sub1 <= l:
        # score += 140
        hard += 1
    elif sub2 <= l:
        # score += 100
        easy += 1


# sort할 필요 없음
# exam.sort(key=lambda x: (x[1], x[0]), reverse=True)

score = min(hard, k) * 140

if hard < k:
    score += min(k-hard, easy) * 100
print(score)
