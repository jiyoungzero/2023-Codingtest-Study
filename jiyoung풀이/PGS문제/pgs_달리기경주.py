# 구현 
# dict 양방향으로 해놓고 풀기 -> gooooooood

def solution(players, callings):
    answer = []
    p_idx_dic = {p:i for i, p in enumerate(players)}
    idx_p_dic = {i:p for i, p in enumerate(players)}
    # print(p_idx_dic, idx_p_dic)

    for c in callings:
        cur_p = c # 추월한 선수
        cur_idx = p_idx_dic[cur_p] # 추월한 선수의 현재 등수

        swap_p = idx_p_dic[cur_idx-1] # 추월 당한 선수
        swap_p_idx = cur_idx-1 # 추월 당한 선수의 등수

        idx_p_dic[swap_p_idx] = cur_p
        idx_p_dic[cur_idx] = swap_p

        p_idx_dic[cur_p] = swap_p_idx
        p_idx_dic[swap_p] = cur_idx

    return list(idx_p_dic.values())