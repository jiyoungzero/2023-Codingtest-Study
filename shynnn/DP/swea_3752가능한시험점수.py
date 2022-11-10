# 경우의 수 2**n개
# 부분집합의 합.. 백트래킹
# 재귀로..?

# def dfs(start, size):
#     sum = 0

#     for i in range(start, start+size):
#         sum += score[i]
#         print(score[i], sum)
#     print('-----')
#     result.add(sum)
#     if start == N-size:
#         print('return')
#         return
#     dfs(start+1, size)


# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     score = list(map(int, input().split()))

#     result = set()

#     for s in range(1, N+1):
#         dfs(0, s)
#     print("result", result)
#     print('#{} {}'.format(t, len(result)))

# combination 풀이
# 런타임 에러
# from itertools import combinations

# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     score = list(map(int, input().split()))
#     result = set()
#     for i in range(N+1):
#         data = list(combinations(score, i))
#         print(combinations(score, i))
#         for j in range(len(data)):
#             sum_data = sum(data[j])
#             result.add(sum_data)
#     print('#{} {}'.format(t, len(result)))


# https://deok2kim.tistory.com/50
# DP 풀이
T = int(input())
for t in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))

    my_score = [0] * (sum(score) + 1)
    # index를 기준으로 나올수 있는 최대값까지 포함할 수 있는 myscore 하기
    my_score[0] = 1  # 0점은 가능하니까 바로 1
    # 점수를 하나하나씩 꺼내서
    for score in score:
        # 만들어둔 리스트의 뒤에서부터 앞으로 하나씩 본다
        # 뒤에서 부터 보는 이유 -> 앞에서부터하면 방금 더해서 얻은 점수를
        # 전에 있던 점수로 인식해서 계속 나아가기 때문
        for i in range(len(my_score) - score, -1, -1):
            # 이미 내가 가능한 점수가 내점수 리스트에 있으면
            if my_score[i]:
                # 그 점수에 방금 얻은 점수를 더해서 그 점수에 해당하는 인덱스를 1로 만든다.
                my_score[i + score] = 1
    print('#{} {}'.format(t, sum(my_score)))