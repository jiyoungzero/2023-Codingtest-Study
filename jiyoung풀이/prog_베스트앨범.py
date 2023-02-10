# 문자열, dict(해쉬)

# 런타임 에러 케이스 많음 
# from collections import defaultdict

# def solution(genres, plays):
#     answer = []
#     music = defaultdict(list) # {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}

#     for g, p in zip(genres, plays):
#         music[g].append((plays.index(p),p))

#     # 플레이 순으로 먼저 정렬해놓기
#     for m in music:
#         music[m].sort(key=lambda x:-x[1])

#     genre_info = []
#     # 가장 많이 재생된 장르 찾기
#     for g in set(genres):
#         genre_info.append([g,sum(music[g][1])])
#     genre_info.sort(key= lambda x :-x[1])
    
    
#     # 장르별로 앞에 있는 거 두개씩
#     for info in genre_info:
#         for best in music[info[0]][0:2]:
#             answer.append(best[0])

#     return answer