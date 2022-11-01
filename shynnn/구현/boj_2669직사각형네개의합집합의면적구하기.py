# 브론즈1 구현
# 시간제한 1초

# 가장 큰 값 구하기
# m = 0
# for i in range(4):
#     m = max(max(arr[i]), m)

graph = [[0] * 101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

answer = 0
for row in graph:
    answer += sum(row)
print(answer)
