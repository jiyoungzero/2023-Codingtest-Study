
# n = int(input())
# ranked = list(map(int, input().split()))
# m = int(input())
# player = list(map(int, input().split()))


# for data in player:
#     ranked.append(data)
#     notRedup_ranked = list(set(ranked))
#     notRedup_ranked.sort(reverse=True)
#     print(notRedup_ranked.index(data)+1)

# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
from bisect import bisect_right

# for문 안에서 append 한 뒤 sort를 해 인덱스를 찾으면 시간초과
# sort - O(nlongn) * for O(n) 따라서 O(n^2logn)
# 미리 정렬을 한 뒤(nlogn 이므로 논외) for 문 안에서는 이진탐색 사용하면 통과
# bisect_right - O(logN) * for O(n) 따라서 O(nlogn)


def climbingLeaderboard(ranked, player):
    answer = []
    ranked = sorted(set(ranked))  # 중복 제거, 정렬

    for score in player:
        answer.append(len(ranked)-bisect_right((ranked), score)+1)
        # bisect_right(arr, target) - arr에 있는 target 오른쪽에 있는 인덱스 반환
    # for data in player:
    #     ranked.append(data)
    #     notRedup_ranked = list(set(ranked))
    #     notRedup_ranked.sort(reverse=True)
    #     answer.append(notRedup_ranked.index(data)+1)
    return answer


if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    for re in result:
        print(re)
