# 난이도 하
# 권장 풀이 시간 30분
# 시간 제한 1초

N, M, K = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))
numbers.sort(reverse=True)
count = [0] * M
result = 0

for _ in range(M):
    if count[0] == K:
        result += numbers[1]
        count[0] = 0
        continue
    result += numbers[0]
    count[0] += 1
print(result)

# 더 간단한 답안 -> 미리 개수 예상해서 시간 줄이기
# second_cnt = M % K
# result = numbers[0] * (M-second_cnt)
# result += numbers[1] * second_cnt
# print(result)
