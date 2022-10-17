# 문제 스스로 풀어보기 
# 26~

# 퀴즈 0 -> 팀이름 (사전순으로--sort 멤버 맞추기), 퀴즈 1 -> 멤버 이름 (팀이름 맞추기)
# 29분 소요

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []

for _ in range(n):
    dict_ele = {}
    name_lst = []
    dict_ele["team_name"] = input()
    dict_ele["ppl_num"] = int(input())
    for _ in range(dict_ele["ppl_num"]):
        name_lst.append(input())
    dict_ele["ppl_name"] = sorted(name_lst) # 사전순으로 정렬

    lst.append(dict_ele)
# print(lst) # [{'team_name': 'twice\n', 'ppl_num': 9, 'ppl_name': ['jihyo\n', 'dahyeon\n', 'mina\n', 'momo\n', 'chaeyoung\n', 'jeongyeon\n', 'tzuyu\n', 'sana\n', 'nayeon\n']}, {'team_name': 'blackpink\n', 'ppl_num': 4, 'ppl_name': ['jisu\n', 'lisa\n', 'rose\n', 'jenny\n']}, {'team_name': 'redvelvet\n', 'ppl_num': 5, 'ppl_name': ['wendy\n', 'irene\n', 'seulgi\n', 'yeri\n', 'joy\n']}]



result = []
# 퀴즈 입력/맞추기
for _ in range(m):
    q = input()
    q_type = int(input())
    
    if q_type == 1: 
        for i in range(len(lst)):
            if q in lst[i]["ppl_name"]:
                result.append(lst[i]["team_name"])
    else:
        for i in range(len(lst)):
            if q in lst[i]["team_name"]:
                for ele in lst[i]["ppl_name"]:
                    result.append(ele)
                    
for ele in result : print(ele, end="")