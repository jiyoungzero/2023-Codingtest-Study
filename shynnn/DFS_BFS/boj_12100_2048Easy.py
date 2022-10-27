# 골드 2
# BFS , map을 돌리는 것이 아닌 상하좌우 옮기기 함수 만들어서도 풀어볼 것
# 아이디어가 없다.. 블로그 참고

# 1. 상하좌우로 이동 시킬 것.
# 2. stack 사용
# 3. 완전 탐색 가능 (4^5) -> 백트래킹?

# ---------------------------------------------
# 정답
# 삼성 A형 공채에서 이런 유형이 많이 나옴
# python으로는 시간이 좀 촉박.
# 최근에 가장 많이 나오는 유형 → 상하좌우가 아닌 Map을 90도 돌리기
# 즉 Left로 이동시키는 함수만 짜고 Map을 90도로 돌린 후 input으로 줌

# deepcopy 함수 : 함수의 내용은 복사, 주소는 복사 안함. 즉 내용은 같으나 완전히 새로운 객체 만들어줌

# 1.rotate 사용해 Map 돌리기 풀이
# 1. DFS + rotate 사용해 Map 돌리기 풀이
# from copy import deepcopy


# def rotate90(b, n):
#     new_b = deepcopy(b)
#     for i in range(n):
#         for j in range(n):
#             new_b[n-1-j][i] = b[i][j]  # 외우기. 90도 돌리는 것!
#     return new_b


# def convert(lst):
#     newlst = [i for i in lst if i]  # lst 안의 양수인 값만 넣은 newlst
#     for i in range(len(newlst)-1):  # -1해줄것. i+1과 비교하는 것이기 때문에 경계값
#         if newlst[i] == newlst[i+1]:
#             newlst[i] = newlst[i]*2
#             newlst[i+1] = 0
#     lst = [i for i in lst if i]  # 다시한번 양수인 값만 넣기
#     return newlst + [0] * (len(lst)-len(newlst))


# def dfs(n, b, cnt):
#     ret = max([max(i) for i in b])
#     if cnt == 0:  # 5번 다 움직였을 경우
#         return ret  # return
#     for _ in range(4):
#         x = [convert(i) for i in b]
#         if b != x:  # 같을 경우에는 더이상 변하지 않는거니까 dfs를 할 필요 없음
#             ret = max(ret, dfs(n, x, cnt-1))
#         b = rotate90(b, n)  # 돌려서 다시. 총 4번
#     return ret


# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]

# print(dfs(n, board, 5))

# ---------------------------------------------
# 2. bfs로 하기
# https://latte-is-horse.tistory.com/349 참고
# 못하겠음~!
