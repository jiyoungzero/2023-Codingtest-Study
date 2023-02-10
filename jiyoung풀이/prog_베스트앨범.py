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

# 정답
from collections import defaultdict

def solution(genres, plays):
    answer = []
    playlist = []
    forplays = defaultdict(list)

    # 각 장르별 총 재생 수 구하기
    for g, p in zip(genres, plays):
        forplays[g].append(p)


    for g_idx, g in enumerate(genres):
        for p_idx, p in enumerate(plays):
            if g_idx == p_idx:
                playlist.append((g_idx, g, p, sum(forplays[g]))) # idx, 장르, 개인플레이수, 장르플레이수

    playlist.sort(key=lambda x:(-x[3], -x[2], x[0]))

    cnt = dict() # 두곡까지만 수록
    for i in set(genres):cnt[i] = 0

    for ele in playlist:
        if cnt[ele[1]] >= 2:continue
        answer.append(ele[0])
        cnt[ele[1]] += 1


    return answer